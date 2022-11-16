import speech_recognition as sr

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
            print('-> ' + r.recognize_google(audio, language='ko-KR'))
        except sr.UnknownValueError:
            print('알 수 없는 에러 발생')
        except sr.RequestError as e:
            print('요청 중 에러 발생: {0}'.format(e))

except KeyboardInterrupt:
    pass

