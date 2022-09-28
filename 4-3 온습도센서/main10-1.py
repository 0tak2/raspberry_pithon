import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

try:
    while True:
        humi, temp = Adafruit_DHT.read_retry(sensor, pin)
        di = (1.8 * temp) - (0.55 * (1 - humi / 100.0) * (1.8 * temp - 26)) + 32
        print(di)
        time.sleep(1)
except KeyboardInterrupt:
    pass
