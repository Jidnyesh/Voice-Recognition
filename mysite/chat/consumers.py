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

machine_info = [
    'one',
    'gate my seen information',
    'get my sin in formation',
    'get machining for me on',
    'get mainington',
    'get much in information',
    'get much in import mason',
    'get much in import mission',
    'get my same information',
    'get my senator mason',
    'get my cuneiform on',
    'i get my chin inflomation',
    'get machine the',
    'got much important',
    'got my shine information',
    'get my shining formation',
    'gave my shining formation',
    'get my ten information',
    'got my shine information',
    'get my ininformed son',
    'get macinoise',
    'get machine information',
    'i gave my senior mason',
    'gave my seeming for a mason',
    'gave me an information',
    'get a hen',
    'gate machines',
    'get machine in formation',
    'i get much an importation',
    'it machine in one may send',
    'i get my cane information',
    'yet my sin information',
    'get mainington mason',
    'get machination',
    'get machine information',
    'at misinformation',
    'gate machine information',
    'got my son in quotation',
    'gate mycening but my son',
    'aggicatin portion',
    'came my seen information',
    'i gave my sending for my son',
    'get the machine information',
    'gave machine details',
    'please get the machine information',
    'i gave my head in for my son',
    'please get the machine on mason',
    'please get to mining formation',
    'please get the machine for me on',
    'please get the machining formation',
    'give machination',
    'give my ininformed on',
    'give my ceninensians',
    'get machine in bornation',
    'gay mycening for mason',
    'it malinaison',
    'i gave my shining for mission',
    'gate mysen information',
    'gate machine for mason',
    'gate much an information',
    'get much in information',
    'get machaon my so',
    'is that the lovers in the gate my inovation',
    'yet marching in formatio',
    'get my shin and t',
    'gad my chainberla',
    'get my chin and for m',
    'get my shin in on missio',
    'yes get my sho',
    'the gas machine i',
    'please get machine th',
    'get machine ye',
    'yet my shame deter',
    'i gave my shindie',
    'get my chin deti',
    'get my chin i di',
    'i got my shin',
    'i gave my shiny di',
    'i get my chin informatio',
    'get my chin in formatio',
    'germain informatio',
    'did my chin and formatio',
    'i gave my chin i',
    'get my chin in formatio',
    'get my sheet',
    'there mad',
    'i get my shine',
    'get my change i',
    'there machine',
    'i get my share ',
    'germaine di',
    'my she',
    'sh',
    'my shi',
    'yet machine ',
    'get machine informatio',
    'get machine in for',
    'get machine in formatio',
    'get my chin in formation',
    'the machine informatio',
    'yet my sin in formatio',
    'get my chin in formatio',
    'did much in informatio',
    'my shin informatio',
    'yet machine informatio',
    'the machine informatio',
    'get machine informatio',
    'get my ten informatio',
    'the much on informatio',
    'yet my shin and',
    'get machin',
    'get machin',
    'yeah get much',
    'get machin',
    'he gave a shor',
    'machin',
    'in detail',
    'i get my shind',
    'did my shindie',
    'i get my sham',
    'get much indigenc',
    'get machin',
    'he get much in de th',
    'get machine i',
    'get my change i',
    'yet my shame d',
    'i get machiner',
    'get machin',
    'get machine detail',
    'gay shade',
    'get machine t',
    'she did ge',
    'get me in nee',
    'my shade',
    'yet my shame need th',
    'get my chin dea',
    'yet to my shine',
    'her machine be d',
    'get on my shee',
    'get to machine',
    'get machine',
    'these get machine th',
    'i gave my shame i di',
    'my shade',
    'my shame he i',
    'my son he di',
    'in my heyda',
    'th',
    'marindi',
    'machine',
    'machine the da',
    'to my shame be di',
    'my shame informatio',
    'machine in formatio',
    'in much in informatio',
    'machine informatio',
    'my chin informatio',
    'machine informatio',
    'get machine informatio',
    'get my chin in formatio',
    'informatio',
    'in formatio',
    'and for m',
    'and formatio',
    'and for the missio',
    'get missing and for m',
    'get me my chi',
    'the main and for me',
    'i seen in for',
    'yet to my son in',
    'germain fo',
    'get the machine i',
    'here to a shini',
    'the machine in format',
    'the main and valiation',
    'did machination',
    'get machine in portman',
    'get machine in fortunation',
    'get machine information',
    'get machine information',
    'get my chin informant',
    'get much in information',
    'dead machine information',
    'get machine in formation',
    'dead machine information',
    'get machine information',
    'i get my son in formation',
    'get my son information',
    'i gave my chin for me so'
    'get machievalian',
    'get my time information',
    'dat machine information',
    'the mission for a mission',
    'i get my side for my son',
    'i gave my then inquired',
    'i get my chin in formation',
    'get my sinecures and ',
    'i get my chin in pertain',
    'get the machine informed',
    'get my shining for mister',
    'dead machination',
    'get my han in potention',
    'i gave my hand information at tea',
    'dead machine in porto',
    'i gave my chin in poitai',
    'dead my sitiwatio',
    'get my chin for the machin',
    'get my chin informatio',
    'dead my shame for the missio',
    'get my senior to me so',
    'at mycening the pertamenia',
    'please cape my machine in for maso',
    'les gave my seeing what amasomi of',
    'please give my mycening formatio',
    'please get my machining for missio',
    'these get medicine for my sudde',
    'get five my shame in forme',
    'locate my my sitting on me t',
    'hello get my machine for',
    'get my shar',
    'did my sending for min',
    'get my sitivatio',
    'get my chin importatio',
    'gay shining formatio',
    'to get my chin in permissio',
    'dead my seeing poiso',
    'did my chinde di',
    'please get my chin need ',
    'please get my hand in for',
    'please get my son i',
    'yes germain',
    'yet for my sin in for m',
    'get my shin informatio',
    'dead my son informatio',
    'get my seminoles',
    'i gave my shining potoma',
    'machine gets',
    'get my senio',
    'get machine inf',
    'again was she importe',
    'i gave my chin ',
    'get my cane in one way sen',
    'but my feet ide',
    'go to my feet i for ',
    'the mysterie',
    'they my seating for maso',
    'only my senior me h',
    'that machine is what was i',
    'it cuisine in for',
    'my he gained when he got ou',
    'but he gave me to g',
    'give me my heated formatio',
    'yes give me my siberian',
    'yes give me my shi',
    'his new me my ininforme',
    'give me my seeming for to me seve',
    'give me my son in portma',
    'give me my ten into making lati',
    'he may an',
    'we ma',
    'i mean my heeding phormio',
    'give me my feeling for me said m',
]

leave_app = [
    'fill my leave appliation',
    'fill my leave form',
    'two',
    'to',
    'feemy leave obligatio',
    'be my leave application',
    'well my devarication',
    'well my leave application',
    'spend my leave application',
    'till my leave obligation',
    'well my leave aplication',
    'parmalee application',
    'but my leave obligation',
    'leave application',
    'leave application',
    'fill my leave obligation',
    'be my leave abnegation',
    'spell my leave obligation',
    'fin my leave habitation',
    'well my leave obligation',
    'ben my leave obligation',
    'a wis my leave application',
    'it is my leave application',
    'is my leave a blithe',
    'well my leave a pleasant',
    'well my leave aplication',
    'tis my leave epigeion',
    'to me i have lichen',
    'pri my le application',
    'is my leave aplication',
]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voices', voices[10].id)
engine.setProperty('rate', 125)


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
        global res

        '''Sending to server'''
        def send():
        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': res,
                # 'response':res_back,
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
            elif res in leave_app:
                print('Say you name: ')
                res = record()
                send()
                print('Say you start date: ')
                res = record()
                send()
                print('Say you end date: ')
                res = record()
                send()
                print('Say you leave type: ')
                res = record()
                send()
                print('Say you leave reason: ')
                res = record()
                send()
                
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

       
        
