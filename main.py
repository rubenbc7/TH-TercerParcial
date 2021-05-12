import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound 
import os
import random
import sys
from gtts import gTTS

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Hable bien wey')
        except sr.RequestError:
            alexa_speak('Contrata un mejor internet che pobre')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):

    if 'Goku play Beatles' in voice_data:
        os.system("taskkill /im chrome.exe /f")
        webbrowser.get().open('https://www.youtube.com/watch?v=Qyclqo_AV2M&list=PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc&ab_channel=TheBeatlesVEVO')
        alexa_speak('Da beatles oh yeah')
    if 'Goku play monkeys' in voice_data:
        os.system("taskkill /im chrome.exe /f")
        webbrowser.get().open('https://www.youtube.com/watch?v=bpOSxM0rNPM&list=PL2XlDsfzN0e5t04gzXwW_UjUuwPwOlNeE&ab_channel=OfficialArcticMonkeys')
        alexa_speak('Ea una de los changos')
    if 'Goku play random' in voice_data:
        os.system("taskkill /im chrome.exe /f")
        webbrowser.get().open('https://www.youtube.com/watch?v=M4vbJQ-MrKo&list=RDMMM4vbJQ-MrKo&start_radio=1&ab_channel=TheBeatlesVEVO')
        alexa_speak('Ahi te van estas')
    if 'Goku play rap' in voice_data:
        os.system("taskkill /im chrome.exe /f")
        webbrowser.get().open('https://www.youtube.com/watch?v=mkiA9tuJ-xM&list=PLx0sYbCqOb8SZSRAN-8zk7JsKAZ5OIpu_&ab_channel=OfficialSaweetie')
        alexa_speak('yeah, the good shit')
    if 'Goku stop' in voice_data:
        os.system("taskkill /im chrome.exe /f")
        alexa_speak('bye bye musica')
    if 'goodbye Goku' in voice_data:
        alexa_speak('Adiós Gohan, tus gustos musicales son malos,  bye bye, xd')
        sys.exit()

time.sleep(1)
alexa_speak('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    print(voice_data)