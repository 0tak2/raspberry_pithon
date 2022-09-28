import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

dhtDevice = adafruit_dht.DHT11(board.D4)

greenLed = 16
blueLed = 20
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

try:
    while True:
        humi = dhtDevice.humidity
        temp = dhtDevice.temperature
        di = (1.8 * temp) - (0.55 * (1 - humi / 100.0) * (1.8 * temp - 26)) + 32
        print("TEMP: ", temp, "'C")
        print("HUMI: ", humi, "%")
        print("DI: ", di)
        print("")

        if di <= 69:
            GPIO.output(greenLed, GPIO.HIGH)
            GPIO.output(blueLed, GPIO.LOW)
            GPIO.output(redLed, GPIO.LOW)
        elif (di >= 70) and (di <= 75):
            GPIO.output(greenLed, GPIO.LOW)
            GPIO.output(blueLed, GPIO.HIGH)
            GPIO.output(redLed, GPIO.LOW)
        elif di >= 76:
            GPIO.output(greenLed, GPIO.LOW)
            GPIO.output(blueLed, GPIO.LOW)
            GPIO.output(redLed, GPIO.HIGH)

        time.sleep(1)

except KeyboardInterrupt:
    print("사용자에 의해 프로그램이 종료되었습니다.")         

finally:
    GPIO.cleanup()
