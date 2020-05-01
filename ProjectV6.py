import speech_recognition as sr
import os
import playsound
import random
import pyowm
import datetime
import webbrowser
import requests
from time import ctime

from gtts import gTTS

r = sr.Recognizer()

def voice_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            response(ask)
        audio = r.listen(source)
        voice_text = ''
        try:
            voice_text = r.recognize_google(audio)
            print(voice_text)
        except:
            response('Sorry could not recognize your voice')

        return voice_text

def response(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000000000000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def weather_temperature():

    weather_key = pyowm.OWM('194d64227dc06cce1c198b75f3e22d9c')
    observation = weather_key.weather_at_place('Boston, US')
    weather = observation.get_weather()
    temperature = weather.get_temperature('fahrenheit')['temp']
    return temperature

def alexa (voice_text):

    if 'your name' in voice_text:
        response('My name is Alexa')

    if 'temperature' in voice_text or 'weather' in voice_text:
        response('The weather is ' + str(weather_temperature()))

    if 'what time is it' in voice_text or 'what time' in voice_text or "what's the time" in voice_text:
        response(just_time())

    if 'date' in voice_text:
        response(just_date())

    if 'open browser' in voice_text:
        search = voice_audio('What website would you like to visit?')
        url = 'https://' + search
        webbrowser.get().open(url)
        response('I found this on the web')

    if 'search' in voice_text:
        search = voice_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        response('I found this on the web')

    if 'tell me a joke' in voice_text:
        response(joke())

    if 'exit' in voice_text:
        exit()

def just_time ():
    x = datetime.datetime.now()
    time_now = (x.strftime("%I:%M:%p"))
    return time_now

def just_date ():
    x = datetime.datetime.now()
    today_date = (x.strftime("%a, %b %d, %Y"))
    return today_date

def joke ():
    r = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    return r.text

response('what can I help you with?')


while True:
    voice_text = voice_audio()
    alexa(voice_text)
