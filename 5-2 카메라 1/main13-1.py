import RPi.GPIO as GPIO
import time

swPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevSwState = 0
newSwState = 0

try:
    while True:
        newSwState = GPIO.input(swPin)
        if newSwState != prevSwState:
            prevSwState = newSwState

            if newSwState == 1:
                print("Click")
            
            time.sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
