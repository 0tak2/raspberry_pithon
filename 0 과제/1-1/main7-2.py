import RPi.GPIO as GPIO
import time

sw1 = 14
sw2 = 15
sw3 = 18
sw4 = 23
sw5 = 24
BUZZER = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261.6)
p.start(50)

try:
    while True:
        if GPIO.input(sw1) == 1:
            p.start(50)
            p.ChangeFrequency(261.6)
        elif GPIO.input(sw2) == 1:
            p.start(50)
            p.ChangeFrequency(293.6)
        elif GPIO.input(sw3) == 1:
            p.start(50)
            p.ChangeFrequency(329.6)
        elif GPIO.input(sw4) == 1:
            p.start(50)
            p.ChangeFrequency(349.2)
        elif GPIO.input(sw5) == 1:
            p.start(50)
            p.ChangeFrequency(391.9)
        else:
            p.stop()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
