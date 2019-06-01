import pyttsx3
import wikipedia
import random
import os
import datetime
import webbrowser
import speech_recognition as sr
import requests


engine = pyttsx3.init()
engine.say('Hello')
engine.runAndWait()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')



engine.setProperty('voices', voices[29].id)
engine.setProperty('rate', 125)


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

machine = [
    'मशीन की इंफॉर्मेशन निकालो',
    'मशीन की पूरी इंफॉर्मेशन निकालो',
    'मशीन की इन पुणे का लो',
    'मशीन की इन्फॉर्म कालो',
    'मशीन का डाटा बताओ',
    'मशीन का डाटा निकालो',
    'मशीन की इंफॉर्मेशन दिखाओ',
    'मशीन के इंफॉर्मेशन दिखाओ',
]
machine_name_select = [
    'sub machine ka data dikhao',
    'sab',
    'sub',
    'sab machine ka data dikhao',
]

recog = [
    'हाय आयुध',
    'हेलो आयुध',
    'सुनो आयुध',
    'चुनाव आयोग',
    'आयुष सुनो',
    'आयुध सुनो',
    'हाय आयोग',
    'सुनो आयुष',
    'सुनो आयुष',
    'सुनवा युद्ध',
    'सुना युद्ध',
    'सोना युद्ध',
    'सुनो युद्ध',
    'सुनवाई युद्ध',
    'हेलो आयुष',
    'सुनो आयोग',
    'हाय आयुक्त',
    
]

  

# obtain audio from the microphone 
def invite():
    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
        # listen for 5 seconds and create the ambient noise energy level  
        r.adjust_for_ambient_noise(source, duration=3)  
        print("Say something!")
        a = r.listen(source)
        
        ma = r.recognize_google(a,language='hi-IN')
        
        print(ma)
        def ayudh():
            r = sr.Recognizer()
            try:
                if ma in recog:
                    print('\nनमस्ते')
                    engine.say("Namaste")
                    engine.runAndWait()

                    with sr.Microphone() as sou:
                        print("आप मुझसे क्या कराना चाहते हैं \n")
                        engine.say("आप मुझसे क्या कराना चाहते हैं")
                        engine.runAndWait()
                        print('Listening')
                        a = r.listen(sou)
                        res1 = r.recognize_google(a,language='hi-IN')

                        try:
                            print("You said:- " + res1)
                            if res1 in date:
                                print('Current time is ',now.hour , now.minute)
                                st = "Current time is {0} slash {1}".format(now.hour,now.minute)
                                engine.say(st)
                                engine.runAndWait()
                            elif res1 in machine:
                                print('आपको कौन सी मशीन डेटा चाहिए')
                                engine.say('आपको कौन सी मशीन डेटा चाहिए')
                                engine.runAndWait()
                                with sr.Microphone() as source:
                                    print('Listening')
                                    a = r.listen(source)
                                    try:
                                        res1 = r.recognize_google(a,language='en-US')
                                        print(res1)
                                        url = 'http://192.168.1.2/api/machines'
                                        r = requests.get(url)
                                        print("You said:- " + res1)
                                        if res1 in machine_name_select:
                                            js = r.json()
                                            for data in js:
                                                print('Machine name -- '+data['name'] + '\n')
                                                print('ID :'+data['id']+'\n')
                                                print('Incharge  \n')
                                                print('Name :'+ data['incharge']['name'] + '\n')
                                                print('Phone :' + data['incharge']['phone'] + '\n')
                                                print('Email :' + data['incharge']['email'] + '\n')
                                                print('Supplier ' + data['supplier']['name'] + '\n')
                                                print("Checkup \n")
                                                print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')
                                        else:
                                            js = r.json()
                                            for data in js:
                                                final = []
                                                nam = data['name']
                                                nam = nam.lower()
                                                for j in nam:
                                                    val = 0
                                                    nam_split = list(j.split())
                                                    res_split = list(res1.split())
                                                    for response1 in res_split:
                                                        if response1 in nam_split:
                                                            val = val + 1
                                                    if val == len(res_split):
                                                        ''.join(nam_split)
                                                        final.append(nam_split)
                                            print(final)
                                    # commands()
                                    except:
                                        print("Could not understand audio")
                                        engine.say('I didnt get that.')
                                        engine.runAndWait()
                                        # commands()

                            # elif res_split[0]=="open" and res_split[1]=="website":
                            #     webst = res_split[2]
                            #     engine.say('Searching for '+webst)
                            #     engine.runAndWait()
                            #     webbrowser.open('https://www.google.com/search?client=firefox-b-ab&q='+webst)
                            # elif res_split[0]=="copy":
                            #     cpd = res_split[1:]
                            #     copied = " ".join(cpd)
                            #     print("this is copied text "+copied)
                            #     pyperclip.copy()
                            # elif res1=='open calculator':
                            #     print('Opening calci')
                            #     os.system('start calc.exe')

                            # elif res1=="break":
                            #     print('fuck')
                        except:
                            print("Could not understand audio")
                            engine.say('I didnt get that.')
                            engine.runAndWait()
                
            except:
                ayudh()
        ayudh()    
        

        # except:
        #     invite()


while True:
    invite()
                