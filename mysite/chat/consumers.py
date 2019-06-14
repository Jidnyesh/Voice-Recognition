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
import pyaudio
import wave

# engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')



# engine.setProperty('voices', voices[29].id)
# engine.setProperty('rate', 125)
machine_info_command = [
    'get machine information',
    'get my she information',
    'get but she information',
    'get my she details',
    'get but she details',
    ]


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
        machine_info_command = ['get machine information']
        machine_cmd_all = ['all','all machine']
        ''' Record Function'''
        global res
        def record():
            
            print('Recording')
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 3
            WAVE_OUTPUT_FILENAME = "output.wav"

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)


            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)


            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            os.system('sox output.wav -c 2 -r 8000 -b 16 soxout.wav')
            res = os.popen('deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio /home/jidnyesh/Downloads/final/mysite/soxout.wav').read()
            print('Done')
            print(res)
            return res
        
        
        '''Machine get command'''
        
        def get_json_byName():
            url = 'http://192.168.1.2/api/machines'
            r = requests.get(url)
            js = r.json()
            for data in js:
                final = []
                nam = data['name']
                nam = nam.lower()
                for j in nam:
                    val = 0
                    nam_split = list(j.split())
                    for response1 in output:
                        if response1 in nam_split:
                            val = val + 1
                    if val == len(res_split):
                        ''.join(nam_split)
                        final.append(nam_split)
            print(final)
            return final

        def get_json_all():
            url = 'http://192.168.1.2/api/machines'
            r = requests.get(url)
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

        def main():
            res = record()
            res_split = res.split()
            if res in machine_cmd_all:
                print('Which machine information you would like to see')
                res = record()
                if res in machine_all_cmd:
                    a = get_json_all()
                    print(a)
                else:
                    a = get_json_byName()
                    if len(final)==0:
                        print('No machine found')
                    elif len(final)==1:
                        url = 'http://192.168.1.2/api/machines'
                        r = requests.get(url)
                        js = r.json()

                    
                    
                    

            

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': res,
            # 'response':res_back,
        }))
