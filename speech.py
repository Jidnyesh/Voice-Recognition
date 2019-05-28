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
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

name = '''
कृपया प्रतीक्षा करें
'''

engine.setProperty('voices', voices[29].id)
engine.setProperty('rate', 125)
engine.say(name)
engine.runAndWait()

'''
List of outcomes
'''
date = [
    'आज की तारीख क्या है',
    'आज की डेट क्या है',
    'तारीख बताओ',
    'अरे भाई तारीख क्या है',
    ]
item_code = [
    'न्यू आइटम कोड जनरेट करो',
    'आइटम कोड जनरेट करो',
    'आइटम का कोड जनरेट करो',
    'न्यू आइटम जनरेट करो',
    
    
    ]
recog = [
    'हाय आयुध',
    'सुनो आयुध',
    'चुनाव आयोग',
    'आयुष सुनो',
    'आयुध सुनो',
    'हाय आयोग',
    'सुनो आयुष'

]

# dictonary = {
#     'कोटेशन दिखाओ':
# }



# obtain audio from the microphone 
def invite():
    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
        # listen for 5 seconds and create the ambient noise energy level  
        r.adjust_for_ambient_noise(source, duration=3)  
        print("Say something!")  
        a = r.listen(source,timeout=4)
        try:
            ma = r.recognize_google(a,language='hi-IN')
            print(ma)
            def ayudh():
                if ma in recog:
                    print('\n नमस्ते')
                    engine.say("Namaste")
                    engine.runAndWait()

                    with sr.Microphone() as source:
                        print("आप मुझसे क्या कराना चाहते हैं \n")
                        engine.say("आप मुझसे क्या कराना चाहते हैं")
                        engine.runAndWait()
                        print('कृपया कहे')
                        a = r.listen(source)
                        res_split = res.split()
                        print(res_split)
                        try:
                            res = r.recognize_google(audio)
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
                                print('fuck') 
                        except :
                            print("Could not understand audio")
                            engine.say('I didnt get that.')
                            engine.runAndWait()
                            ayudh()
        except:
            invite()

while True:
    invite()
                