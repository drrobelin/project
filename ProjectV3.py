import speech_recognition as sr
import os
import playsound
import random
import pyowm

from gtts import gTTS

r = sr.Recognizer()

def voice_audio():
    with sr.Microphone() as source:
        response('what can I help you with?')
        audio = r.listen(source)
        voice_text = ''
        try:
            voice_text = r.recognize_google(audio)

        except:
            response('Sorry could not recognize your voice')
            (exit())
        return voice_text

def response(audio_string):
    text_to_speech = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 10000000000000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def weather_temperature():

    weather_key = pyowm.OWM('194d64227dc06cce1c198b75f3e22d9c')
    observation = weather_key.weather_at_place('Boston, US')
    weather = observation.get_weather()
    temperature = weather.get_temperature('fahrenheit') ['temp']
    return temperature

def alexa (voice_text):
    if 'your name' in voice_text:
        response('My name is Alexa')
    if 'temperature' or 'weather' in voice_text:
        response('The weather is ' + str(weather_temperature()))


voice_text = voice_audio()
print (voice_text)
alexa(voice_text)
