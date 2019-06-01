global v
v = 1
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


machine = [
    'मशीन की इंफॉर्मेशन निकालो',
    'मशीन की पूरी इंफॉर्मेशन निकालो',
    'मशीन की इन पुणे का लो',
    'मशीन की इन्फॉर्म कालो',
    'मशीन का डाटा बताओ',
    'मशीन का डाटा निकालो',
    'मशीन की इंफॉर्मेशन दिखाओ',
    'मशीन के इंफॉर्मेशन दिखाओ',
    'मशीन की इंफॉर्मेशन निकालो',
]

machine_name_select = [
    'sub machine ka data dikhao',
    'sab',
    'sub',
    'sab machine ka data dikhao',
    'sab sab'
]



def listen_this():
    global res,r,a
    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Please wait. Calibrating microphone...")  
        # listen for 5 seconds and create the ambient noise energy level  
        r.adjust_for_ambient_noise(source, duration=3)  
        print("Say something!")
        a = r.listen(source)
        if v==3:
            res = r.recognize_google(a)
        else:
            res = r.recognize_google(a,language='hi-IN')
        return res


def ayudh():
    print('\nनमस्ते')
    a = 'Namaste'
    b = 'Aap muzse kya karana chahte hai'
    engine.say("Namaste")
    engine.say("आप मुझसे क्या कराना चाहते हैं")
    engine.runAndWait()
    return a,b

def commands():
    print('आपको कौन सी मशीन डेटा चाहिए')
    ex = 'आपको कौन सी मशीन डेटा चाहिए'
    engine.say('आपको कौन सी मशीन डेटा चाहिए')
    engine.runAndWait()
    v = 3
    return ex

        
def machine_data():
    url = 'http://192.168.1.2/api/machines'
    r = requests.get(url)
    if res in machine_name_select:
        js = r.json()
        for data in js:
            jsonk = 'Json data got'
            print('Machine name -- '+data['name'] + '\n')
            print('ID :'+data['id']+'\n')
            print('Incharge  \n')
            print('Name :'+ data['incharge']['name'] + '\n')
            print('Phone :' + data['incharge']['phone'] + '\n')
            print('Email :' + data['incharge']['email'] + '\n')
            print('Supplier ' + data['supplier']['name'] + '\n')
            print("Checkup \n")
            print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')
        return jsonk
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
        val = 1
        return final
                        

                
        


    
while True:
    
    listen_this()
    if res in recog:
        ayudh()
        v = 2
    elif res in machine and v==2:
        commands()
        v = 3
    elif res in machine_name_select and v==3:
        machine_data()
        v = 1
    print(res)
    if v:
        print(v)

