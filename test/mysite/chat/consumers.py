from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

#test3
import pyttsx3
import wikipedia
import random
import os
import datetime
import webbrowser
import speech_recognition as sr
import requests

engine = pyttsx3.init()

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
    'ब्लू आइज',
    'हेलो आयुष',
    'सुनो आयोग',
    'हाय आयुक्त',
    'आयुध',
    'हाय',
    'सोनू आयोग',
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

##--##

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        # message = event['message'
        
        def listen_this():
            global res,r,a
            r = sr.Recognizer()  
            with sr.Microphone() as source:  
                # print("Please wait. Calibrating microphone...")  
                # listen for 5 seconds and create the ambient noise energy level  
                r.adjust_for_ambient_noise(source, duration=3)  
                print("Say something!")
                a = r.listen(source)
                # if second:
                #     res = r.recognize_google(a)
                # else:
                res = r.recognize_sphinx(a)
                return res


        def ayudh():
            print('\nनमस्ते')
            a = 'Namaste'
            res_back = 'आप मुझसे क्या कराना चाहते हैं'
            engine.say("Namaste")
            engine.say("आप मुझसे क्या कराना चाहते हैं")
            engine.runAndWait()

        def commands():
            res_back = 'आपको कौन सी मशीन डेटा चाहिए'
            engine.say('आपको कौन सी मशीन डेटा चाहिए')
            engine.runAndWait()
            

                
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
                
                return final
                                
        def mainf():
            global res_back
            res_back = ''
            listen_this()
            if res in recog:
                ayudh()
                res_back = 'आप मुझसे क्या कराना चाहते हैं'
                
            elif res in machine:
                
                commands()
                res_back = 'आपको कौन सी मशीन डेटा चाहिए'
                    
            elif res in machine_name_select:
                
                machine_data()
                res_back = 'le bc kha'
                    
            print(res)
            print(res_back)
            
        
        mainf()

            
        
        res = 'random test'

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': res,
            'response':res_back,
        }))
