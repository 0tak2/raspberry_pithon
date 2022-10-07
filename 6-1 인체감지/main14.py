import RPi.GPIO as GPIO
import time

pirPin = 16


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        sensorValue = GPIO.input(pirPin)
        print(sensorValue)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
