import RPi.GPIO as GPIO
import time

sw1 = 14
sw2 = 15
sw3 = 18
sw4 = 23
sw5 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(sw1) == 1:
            print("sw1")
        elif GPIO.input(sw2) == 1:
            print("sw2")
        elif GPIO.input(sw3) == 1:
            print("sw3")
        elif GPIO.input(sw4) == 1:
            print("sw4")
        elif GPIO.input(sw5) == 1:
            print("sw5")
        else:
            pass

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
