import speech_recognition as sr
import RPi.GPIO as GPIO

greenLed = 16
blueLed = 20
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

def handleLed(greenOn, blueOn, redOn):
    if greenOn == 1:
        GPIO.output(greenLed, 1)
    elif greenOn == 0:
        GPIO.output(greenLed, 0)

    if blueOn == 1:
        GPIO.output(blueLed, 1)
    elif blueOn == 0:
        GPIO.output(blueLed, 0)

    if redOn == 1:
        GPIO.output(redLed, 1)
    elif redOn == 0:
        GPIO.output(redLed, 0)

try:
    while True:
        # 마이크를 통해 음성 녹음
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('아무거나 말해보세요!')
            audio = r.listen(source)

        # Google Speech Recognition를 통한 음성 인식
        try:
            # 기본키를 사용하지 않고 키를 지정하려면 r.recognize_google(audio, key='KEY')
            text = r.recognize_google(audio, language='ko-KR')
            print('-> ' + text)

            if text in '빨간색':
                handleLed(0, 0, 1)
            elif text in '파란색':
                handleLed(0, 1, 0)
            elif text in '초록색' or text in '녹색':
                handleLed(1, 0, 0)
            elif text in '꺼':
                handleLed(0, 0, 0)

        except sr.UnknownValueError:
            print('알 수 없는 에러 발생')
        except sr.RequestError as e:
            print('요청 중 에러 발생: {0}'.format(e))

except KeyboardInterrupt:
    pass

GPIO.cleanup()
