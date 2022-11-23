from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from datetime import datetime
from ..db import get_db

api_bp = Blueprint('hydration', __name__, url_prefix='/api/hydration')
api = Api(api_bp)

class Hydration(Resource): # /api/hydration
    def get(self):
        return { 'success': True }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('time', type=str, required=True, location='json')
        parser.add_argument('value', type=str, required=True, location='json')

        args = parser.parse_args()
        time, value = args.values()

        try:
            time_parsed = datetime.strptime(time + " +0900", '%Y-%m-%d %H:%M:%S %z')
        except ValueError:
            error = '형식에 맞지 않는 시간입니다. 올바른 형태: %Y-%m-%d %H:%M:%S'
            return {
                'success': False,
                'payload': {
                    'type': 'tds',
                    'time': time,
                    'value': value
                },
                'error': str(error)
            }, 400
        time_str = time_parsed.strftime("%Y-%m-%d %H:%M:%S %z")

        print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] New Volume data (time="{time_str}" value={value})')

        # 우선 데이터베이스에서 이전 볼륨 값을 읽는다 // TO DO: 여기부터 계속
        db = get_db()
        cursor = db.cursor()
        try:
            id, created, differ, current_vol = cursor.execute("SELECT * FROM hydration ORDER BY id DESC").fetchone()
            print(id, created, differ, current_vol)
        except Exception as e:
            error = '이전 값을 불러오는 중 오류가 발생했습니다.'
            print(error + str(e))
            return {
                'success': False,
                'payload': {
                    'type': 'tds',
                    'time': time,
                    'value': value
                },
                'error': str(error)
            }, 500

        # 데이터베이스에 값 추가 인서트
        error = None
        try:
            db.execute(
                "INSERT INTO hydration (created, tds) VALUES (?, ?)",
                (time_str, int(value)),
            )
            db.commit()
        except Exception as e:
            print(e)
            error = e

        if error == None:
            return {
                'success': True,
                'payload': {
                    'type': 'tds',
                    'time': time,
                    'value': value
                }
            }, 200
        else:
            return {
                'success': False,
                'payload': {
                    'type': 'tds',
                    'time': time,
                    'value': value
                },
                'error': str(error)
            }, 500

api.add_resource(Hydration, '')