from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


#test3
from fpdf import FPDF
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


machine_cmd_all = ['all','all machine','get all of it']




engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voices', voices[10].id)
engine.setProperty('rate', 125)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        p = os.getcwd()
        print(p)
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
        global res
        with open('machine_info.txt','r') as f:
            machine_info = f.read()
            f.close()
        with open('leave_app_call.txt','r') as f:
            leave_app_call = f.read()
            f.close()
        '''Sending to server'''
        def send():
        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': res,
                # 'response':res_back,
            }))
        def send_leave(leave_msg):
            self.send(text_data=json.dumps({
                'leave_msg': leave_msg,
            }))

        '''Printing to PDF'''
        def add_pdf(name,start,end,ltype,reason):
            main = f'''
            Name : {name}\n
            Duration : {start} - {end}\n
            Type of leave : {ltype}\n
            Reason : {reason}\n
            '''
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=main, ln=1, align="C")
            pdf.output("simple_demo.pdf")
            print('PDF succesfully generated in Your pc')

        '''For printing json data'''
        def print_json(data):
            print('Machine name -- '+data['name'] + '\n')
            print('ID :'+data['id']+'\n')
            print('Incharge  \n')
            print('Name :'+ data['incharge']['name'] + '\n')
            print('Phone :' + data['incharge']['phone'] + '\n')
            print('Email :' + data['incharge']['email'] + '\n')
            print('Supplier ' + data['supplier']['name'] + '\n')
            print("Checkup \n")
            print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')
          

        def get_json_byName():
            js = parse_json()
            res_split = res.split()
            for data in js:
                final = []
                nam = data['name']
                nam = nam.lower()
                nam = ''.join(nam)
                print(nam)
                for j in nam:
                    val = 0
                    nam_split = j.split()
                    
                    for response1 in res:
                        if response1 in nam_split:
                            val = val + 1
                    if val == len(res_split):
                        ''.join(nam_split)
                        final.append(nam_split)
            print(final)
            return final

        def get_json_all():
            js = parse_json()
            for data in js:
                print_json(data)

        '''Json parser'''
        def parse_json():
            url = 'http://192.168.1.2/api/machines'
            r = requests.get(url)
            js = r.json()
            return js

        '''Find machine'''
        def find_machine(final):
            if len(final)==0:#For length of detected name when 0
                print('No machine found')
                print()
            elif len(final)==1:#For length of detected name when 1
                js = parse_json()
                for data in js:
                    if data['name']==final[0]:
                        print_json(data)
            else:#For length of detected name when more than 1
                js = parse_json()
                for data in js:
                    for i in range(len(final)):
                        print(i+1 + ':- '+final[i])
        '''Machine get command'''
        def main():
            res = record()
            send()
            print('orignal -- '+res)

            if res=='':
                print('I cannot hear you')
                engine.say("Sorry , I cannot hear you")
                engine.runAndWait()

            elif res in machine_info: #First command if we ask for machine information
                res = 'Get machine information'
                print(res+'\n\n')
                print('Which machine information you would like to see\n\n')
                engine.say("Which machine information you want")
                engine.runAndWait()
                res = record()
                send()
                if res in machine_cmd_all:
                    get_json_all()
                else:
                    final = get_json_byName()
                    find_machine(final)

            elif res in leave_app_call:
                send_leave(leave_msg = 'True')
                print('Say you name: ')
                res = record()
                i1 = res
                send_leave(leave_msg = res)
                print('Say you start date: ')
                res = record()
                i2 = res
                send_leave(leave_msg = res)
                print('Say you end date: ')
                res = record()
                i3 = res
                send_leave(leave_msg = res)
                print('Say you leave type: ')
                res = record() 
                i4 = res
                send_leave(leave_msg = res)
                print('Say you leave reason: ')
                res = record()
                i5 = res
                send_leave(leave_msg = res)
                
                add_pdf(i1,i2,i3,i4,i5)

            else:
                print('Not found')
            
        ''' Record Function'''
        def record():
            global res
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
            res = os.popen('deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio /home/jidnyesh/Downloads/final/Voice-Recognition/mysite/soxout.wav').read()
            print('Done')
            lis_res = list(res)
            res = ''.join(lis_res[:-1])
            print(res)
            return res
        
        main()

       
        
