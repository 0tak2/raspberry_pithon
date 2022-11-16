import requests
import re
import json

jsonFile = open('token.json', encoding='utf-8')
jsonDict = json.load(jsonFile)
token = jsonDict['token']

url = f'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={token}&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
response = requests.get(url, verify=False) # SSL 인증서 관련 예외가 발생하여 인증서 검증을 생략하도록 지정함

pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>', response.text)
pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>', response.text)
stationName = re.findall(r'<stationName>(.+)</stationName>', response.text)


def indexPrompt() -> int:
    print("* 조회할 수 있는 자치구 목록")
    print(*stationName)
    query = input("* 조회할 자치구 이름 입력: ")

    try:
        index = stationName.index(query)
    except ValueError:
        print("! 잘못된 값을 입력했습니다. 다시 입력해주세요.")
        index = -1

    return index

def main():
    while True:
        index = indexPrompt()
        if index != -1:
            break

    print(f'[{stationName[index]}의 미세먼지 정보]')
    print(f'- PM10: {pm10[index]}')
    print(f'- PM25: {pm25[index]}')

main()
