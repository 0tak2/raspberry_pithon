import RPi.GPIO as GPIO
import time
import picamera
import datetime

swPin = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevSwState = 0
newSwState = 0

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

try:
    while True:
        newSwState = GPIO.input(swPin)
        if newSwState != prevSwState:
            prevSwState = newSwState

            if newSwState == 1:
                now = datetime.datetime.now()
                print(now)
                fileName = now.strftime('%Y-%m-%d %H%M%S %f') + '.jpg'
                camera.capture(fileName)
                print(fileName + " saved \n")
            
            time.sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
