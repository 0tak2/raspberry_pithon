import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

dhtDevice = adafruit_dht.DHT11(board.D4)

greenLed = 16
blueLed = 20
redLed = 21

try:
    while True:
        humi = dhtDevice.humidity
        temp = dhtDevice.temperature
        di = (1.8 * temp) - (0.55 * (1 - humi / 100.0) * (1.8 * temp - 26)) + 32
        print("TEMP: ", tmep)
        print("HUMI: ", humi)
        print("DI: ", di)

        if di<=69:
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
    pass         
