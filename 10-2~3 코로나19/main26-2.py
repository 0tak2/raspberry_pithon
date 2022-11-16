import requests
import re
import json
import datetime

jsonFile = open('token.json', encoding='utf-8')
jsonDict = json.load(jsonFile)
token = jsonDict['token']

today = datetime.datetime.now().strftime('%Y%m%d')

# [DEPRECATED] 아래 API는 2023-2-11부터 서비스 중단
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={token}&pageNo=1&numOfRows=30&startCreateDt={today}&endCreateDt={today}'
response = requests.get(url) 

gubun = re.findall(r'<gubun>(.+?)</gubun>', response.text)
incDec = re.findall(r'<incDec>(.+?)</incDec>', response.text)

totalIndex = gubun.index('합계')

print('오늘 날짜: ' + today)
print('확진자 합계: ' + incDec[totalIndex])
