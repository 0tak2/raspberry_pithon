import time
import datetime

try:
    while True:
        now = datetime.datetime.now()
        print(now)
        f = open('temphumi.txt', 'a')
        f.write(str(now) + '\r\n')
        f.close()
        time.sleep(1.0)
except KeyboardInterrupt:
    pass
finally:
    pass
