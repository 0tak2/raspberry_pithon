from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

@app.route('/')
def main():
    return render_template("index.html") 

@app.route('/data', methods=['POST'])
def handleData():
    data = request.form['led']

    if data == 'on':
        GPIO.output(ledPin, GPIO.HIGH)
        return main()
    elif data == 'off':
        GPIO.output(ledPin, GPIO.LOW)
        return main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
