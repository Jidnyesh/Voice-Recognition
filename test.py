import pyttsx3
import os
import speech_recognition as sr


engine = pyttsx3.init()
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
recog = [
    'हाय आयुध',
    'सुनो आयुध',
    'चुनाव आयोग',
    'आयुष सुनो',
    'आयुध सुनो',
    'हाय आयोग',
    'सुनो आयुष'

]



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
            
        except:
            invite()

while True:
    invite()
                