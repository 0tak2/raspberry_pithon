from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

@app.route('/')
def main():
    return "hello Flask"

@app.route('/ledon')
def ledOn():
    GPIO.output(ledPin, GPIO.HIGH)
    return '<h1>LED ON</h1>'

@app.route('/ledoff')
def ledOff():
    GPIO.output(ledPin, GPIO.LOW)
    return '<h1>LED OFF</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
