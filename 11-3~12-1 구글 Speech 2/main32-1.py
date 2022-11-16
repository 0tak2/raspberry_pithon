import requests
import re
import os
import time

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144063000'

def speak(msg, option='-s 160 -p 50 -a 200 -v ko+f5'):
    os.system("espeak {} '{}'".format(option, msg))

try:
    while True:
        response = requests.get(url)
        temp = re.findall(r'<temp>(.+)</temp>', response.text)
        humi = re.findall(r'<reh>(.+)</reh>', response.text)
        msg = f'기온은 {temp[0].split(".")[0]} 도이고, 습도는 {humi[0]} 퍼센트 입니다.'
        speak(msg)
        time.sleep(10)

except KeyboardInterrupt:
    pass

