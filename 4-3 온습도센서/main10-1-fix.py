import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D4)

try:
    while True:
        humi = dhtDevice.humidity
        temp = dhtDevice.temperature
        di = (1.8 * temp) - (0.55 * (1 - humi / 100.0) * (1.8 * temp - 26)) + 32
        print(di)
        time.sleep(1)
except KeyboardInterrupt:
    pass         
