import os
import datetime

def speak(msg, option='-s 180 -p 50 -a 200 -v ko+f5'):
    log(f'espeak {option} {msg}')
    os.system("espeak {} '{}'".format(option, msg))

def log(contents):
    print(f'[{datetime.datetime.now()}] {contents}')

speak("안녕하세요. 임영택입니다.")
