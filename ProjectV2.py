import speech_recognition as sr
import os
import playsound
from gtts import gTTS

r = sr.Recognizer()

def voice_audio():
    with sr.Microphone() as source:
        print('What can I help you with?')
        response('what can I help you with?')
        audio = r.listen(source)

        try:
            voice_text = r.recognize_google(audio)
            print(voice_text)
        except:
            print('Sorry could not recognize your voice')


def response(text):
    text_to_speech = gTTS(text = text, lang = 'en')
    text_to_speech.save('response.mp3')
    playsound.playsound('response.mp3')


voice_audio()

