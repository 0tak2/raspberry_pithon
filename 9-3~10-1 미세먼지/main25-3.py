import requests
import re
import json
import RPi.GPIO as GPIO
import time
import urllib3

# 토큰 및 요청 URL 세팅
jsonFile = open('token.json', encoding='utf-8')
jsonDict = json.load(jsonFile)
token = jsonDict['token']
url = f'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={token}&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
urllib3.disable_warnings() # requests.get() 시 verfy=False 인자 지정으로 경고가 나오는 것을 숨김

# GPIO 초기화
greenLed = 16
blueLed = 20
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

def getAllPmData() -> tuple:
    response = requests.get(url, verify=False) # SSL 인증서 관련 예외가 발생하여 인증서 검증을 생략하도록 지정함
    pm10 = re.findall(r'<pm10Value>(.+)</pm10Value>', response.text)
    pm25 = re.findall(r'<pm25Value>(.+)</pm25Value>', response.text)
    stationName = re.findall(r'<stationName>(.+)</stationName>', response.text)
    dataTime = re.findall(r'<dataTime>(.+)</dataTime>', response.text)

    return (pm10, pm25, stationName, dataTime)

def getOnePmData(index) -> tuple:
    all_pm10, all_pm25, all_stationName, all_dataTime = getAllPmData()
    return (all_pm10[index], all_pm25[index], all_stationName[index], all_dataTime[index])

def indexPrompt(stationName) -> int:
    print("* 조회할 수 있는 위치 목록")
    print(*stationName)
    query = input("* 조회할 자치구 위치 입력: ")

    try:
        index = stationName.index(query)
    except ValueError:
        print("! 잘못된 값을 입력했습니다. 다시 입력해주세요.")
        index = -1

    return index

def handleLed(color): # 0: Green, 1: Blue, 2: Red, 3: All
    if color == 0:
        GPIO.output(greenLed, GPIO.HIGH)
        GPIO.output(blueLed, GPIO.LOW)
        GPIO.output(redLed, GPIO.LOW)
    elif color == 1:
        GPIO.output(greenLed, GPIO.LOW)
        GPIO.output(blueLed, GPIO.HIGH)
        GPIO.output(redLed, GPIO.LOW)
    elif color == 2:
        GPIO.output(greenLed, GPIO.LOW)
        GPIO.output(blueLed, GPIO.LOW)
        GPIO.output(redLed, GPIO.HIGH)
    elif color == 3:
        GPIO.output(greenLed, GPIO.HIGH)
        GPIO.output(blueLed, GPIO.HIGH)
        GPIO.output(redLed, GPIO.HIGH)
    else:
        GPIO.cleanup()
        raise Exception('잘못된 인수를 받았습니다.')

def GPIOLoop(index):
    try:
        while True:
            pm10, pm25, stationName, dataTime = getOnePmData(index)
            print()
            print(f'[{stationName}의 미세먼지 정보를 업데이트했습니다.]')
            print(f'- 기준시간: {dataTime}')
            print(f'- PM10: {pm10}')
            print(f'- PM25: {pm25}')

            pm25_int = int(pm25)
            if pm25_int <= 30:
                handleLed(0)
                print(f'- 대기질 좋음')
            elif pm25_int >= 31 and pm25_int <= 80:
                handleLed(1)
                print(f'- 대기질 보통')
            elif pm25_int >= 81 and pm25_int <= 150:
                handleLed(2)
                print(f'- 대기질 나쁨')
            elif pm25_int >= 151:
                handleLed(3)
                print(f'- 대기질 매우 나쁨')

            time.sleep(60)

    except KeyboardInterrupt:
        pass

def main():
    temp1, temp2, stationName, dataTime = getAllPmData()
    index = -1
    while True:
        index = indexPrompt(stationName)
        if index != -1:
            break

    GPIOLoop(index)
    GPIO.cleanup()

main()
