import speech_recognition as sr
import requests
import re
import os
import time

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144063000'

def getWeather():
    response = requests.get(url)
    temp = re.findall(r'<temp>(.+)</temp>', response.text)
    humi = re.findall(r'<reh>(.+)</reh>', response.text)
    return (temp, humi)

def speak(msg, option='-s 160 -p 50 -a 200 -v ko+f5'):
    os.system("espeak {} '{}'".format(option, msg))

try:
    while True:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("날씨라고 말하면 현재 날씨를 알려줍니다")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ko-KR')
            print("-> " + text)
            if text in '날씨':
                print("날씨 명령을 인식하였습니다.")
                
                temp, humi = getWeather()
                msg = f'기온은 {temp[0].split(".")[0]} 도이고, 습도는 {humi[0]} 퍼센트 입니다.'
                speak(msg)

        except sr.UnknownValueError:
            print('죄송합니다. 이해하지 못했습니다.')
        
        except sr.RequestError as e:
            print('서버에 요청하는 도중 오류가 발생했습니다: {0}'.format(e))

except KeyboardInterrupt:
    pass

