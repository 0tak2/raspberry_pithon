import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.capture('test1.jpg')

