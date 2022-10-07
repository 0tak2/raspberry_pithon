import RPi.GPIO as GPIO
import time
import picamera
import datetime

pirPin = 16


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

try:
    while True:
        sensorValue = GPIO.input(pirPin)
        if sensorValue == 1:
            now = datetime.datetime.now()
            print(now)
            fileName = 'imgs/' + now.strftime('%Y-%m-%d %H%M%S') + '.jpg'
            camera.capture(fileName)
            time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
