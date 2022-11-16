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
            text = r.recognize_google(audio, language='ko-KR')
            print('-> ' + text)

            if text in "날씨":
                print("날씨 명령을 인식했습니다.")
        except sr.UnknownValueError:
            print('이해하지 못했습니다.')
        except sr.RequestError as e:
            print('요청 중 에러 발생: {0}'.format(e))

except KeyboardInterrupt:
    pass

