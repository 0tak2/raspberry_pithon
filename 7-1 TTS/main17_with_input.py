import os
import datetime

def speak(msg, option='-s 180 -p 50 -a 200 -v ko+f5'):
    log(f'espeak {option} {msg}')
    os.system("espeak {} '{}'".format(option, msg))

def log(contents):
    print(f'[{datetime.datetime.now()}] {contents}')

try:
    while True:
        speak(input())
except KeyboardInterrupt:
    log("사용자에 의해 종료되었습니다")
