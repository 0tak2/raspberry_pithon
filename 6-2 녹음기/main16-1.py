# python3 실행시 sudo를 통해 실행하면 pyaudio가
# usb 마이크를 인식하지 못하고 오류를 발생시키는
# 문제가 있다.
# sudo를 사용하지 말 것.
# python3 main16-2.py

import RPi.GPIO as GPIO
import time

swPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

oldSw = 0
newSw = 0

try:
    while True:

        newSw = GPIO.input(swPin)
        if newSw != oldSw:
            oldSw = newSw

            if newSw == 1:
                print("click")

            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
