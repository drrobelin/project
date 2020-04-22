import speech_recognition as sr

r = sr.Recognizer()


def voice_audio():
    with sr.Microphone() as source:
        print('What Can I Help you with?')
        audio = r.listen(source)

        try:
            voice_text = r.recognize_google(audio)
            print(voice_text)
        except:
            print('Sorry could not recognize your voice')

voice_audio()
