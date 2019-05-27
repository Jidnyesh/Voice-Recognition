import pyttsx3
import wikipedia
import random
import os
import datetime
import webbrowser
import speech_recognition as sr
import pyperclip
pyperclip.copy('Copied text 1')

engine = pyttsx3.init()
engine.say("Hello jidnyesh  , welcome back")
engine.setProperty('rate',120)
engine.setProperty('volume',0.9)
engine.runAndWait()

'''
List of outcomes
'''
date = [
    'get the current date',
    'get the current time',
    'what is the current time',
    'what is the time',
    ]
google = [
    'open Google',
    'open Google dot com',
    'open google.com',
    'search Google',
    ]
recog = [
    'hi jarvis',
    'Hi Jarvis',
    'hi larvis',
    'hi Jarvis'

]
def main():
    while True:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        print('Listening')
        with sr.Microphone() as s:
            a = r.listen(s,timeout=3)
            ma = r.recognize_google(a)
            print(ma)
            if ma in recog:
                print('hi this is Jarvis')
                engine.say("Hi this is bi frost")
                engine.runAndWait()
                with sr.Microphone() as source:
                    print("Tell me something:")
                    engine.say("Tell me something")
                    engine.runAndWait() 
                    audio = r.listen(source)
                    res = r.recognize_google(audio)
                    res_split = res.split()
                    print(res_split)
                    try:
                        print("You said:- " + res)
                        if res in date:
                            print('Current time is ',now.hour , now.minute)
                            st = "Current time is {0} slash {1}".format(now.hour,now.minute)
                            engine.say(st)
                            engine.runAndWait()
                        elif res in google:
                            engine.say('Opening google.com')
                            engine.runAndWait()
                            webbrowser.open('https://www.google.com')
                        elif res_split[0]=="open" and res_split[1]=="website":
                            webst = res_split[2]
                            engine.say('Searching for '+webst)
                            engine.runAndWait()
                            webbrowser.open('https://www.google.com/search?client=firefox-b-ab&q='+webst)
                        elif res_split[0]=="copy":
                            cpd = res_split[1:]
                            copied = " ".join(cpd)
                            print("this is copied text "+copied)
                            pyperclip.copy()
                        elif res=='open calculator':
                            print('Opening calci')
                            os.system('start calc.exe')

                        elif res=="break":
                            main() 
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                        engine.runAndWait()
            
main()