import RPi.GPIO as GPIO
import time

BUZZER = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261.6)
p.start(50)

try:
    while True:
        p.start(50)
        p.ChangeFrequency(261.6)
        time.sleep(1.0)
        p.ChangeFrequency(293.6)
        time.sleep(1.0)
        p.ChangeFrequency(329.6)
        time.sleep(1.0)
        p.ChangeFrequency(349.2)
        time.sleep(1.0)
        p.ChangeFrequency(391.9)
        time.sleep(1.0)
        p.stop()
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
