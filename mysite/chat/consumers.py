from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


#test3
from fpdf import FPDF
import pyttsx3
import wikipedia
import random
import os
import time
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
        print(message)
        # Send message to room group
        if message=='hell':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        else:
            print('runned')

    # Receive message from room group
    def chat_message(self, event):
        global res

        #To import list from machine_info.txt
        with open('machine_info.txt','r') as f:
            machine_info_list = f.read()
            f.close()

        #To import list from leave_app_call.txt
        with open('leave_app_call.txt','r') as f:
            leave_app_call = f.read()
            f.close()

        '''Sending to server'''
        #Sending message converted
        def send():
            self.send(text_data=json.dumps({
                'message': res,
                # 'response':res_back,
            }))
        #Sending leaveform status
        def send_leaveform_status(leave_msg):
            self.send(text_data=json.dumps({
                'leave_msg': leave_msg,
            }))
        #Sending leave application form fields
        def send_name(leave_name,status):
            self.send(text_data=json.dumps({
                'leave_name': leave_name,
                'status':status,
            }))
        #sending machine info status and machine info
        def send_machine_info_status(machine_info,statusm):
            self.send(text_data=json.dumps({
                'machine_info_status':machine_info,
                'statusm':statusm,
            }))
        #Send page reload information
        def send_reload(reloadp):
            self.send(text_data=json.dumps({
                'reloadp':reloadp,
            }))

        
        '''Printing to PDF'''
        def add_pdf(name,address,start,end,ltype,reason):
            name = f'Name : {name}'
            address = f'Address : {address}'
            duration = f'Duration of leave : {start} - {end}'
            ltype = f'Type of leave : {ltype}'
            reason = f'Reason : {reason}'
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=name, ln=1, align="C")
            pdf.cell(200, 10, txt=address, ln=2, align="C")
            pdf.cell(200, 10, txt=duration, ln=3, align="C")
            pdf.cell(200, 10, txt=ltype, ln=4, align="C")
            pdf.cell(200, 10, txt=reason, ln=5, align="C")
            pdf.output("simple_demo.pdf")
            print('PDF succesfully generated in Your pc')

        '''For printing json data'''
        def print_json(data):
            main = f'''
            Machine name -- {data['name']}\n
            ID : {data['id']}
            Incharge \n
            Name : {data['incharge']['name']}
            '''
            print('Machine name -- '+data['name'] + '\n')
            print('ID :'+data['id']+'\n')
            print('Incharge  \n')
            print('Name :'+ data['incharge']['name'] + '\n')
            print('Phone :' + data['incharge']['phone'] + '\n')
            print('Email :' + data['incharge']['email'] + '\n')
            print('Supplier ' + data['supplier']['name'] + '\n')
            print("Checkup \n")
            print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')
            return main
        #GEtting json output by name 
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
                main = print_json(data)
                return main

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
        '''Leave application function'''
        def leave_form():
            
            send_leaveform_status(leave_msg = 'True')
            print('You now will tell me your information')
            engine.say("You now will tell me your information")
            engine.runAndWait()
            time.sleep(1)
        def confirm():
            engine.say("Is this information correct")
            engine.runAndWait()
            conf = record()
            return conf
        #
        def leave_name():
            # send_boxinfo(box="Can you please let me know your name")
            engine.say("Can you please let me know your name")
            engine.runAndWait()
            print('Say your name: ')
            res = record()
            i1 = res
            return i1
        def leave_address():
            engine.say("Can you please let me know your address")
            engine.runAndWait()
            print('Say your Address: ')
            res = record()
            iadd = res
            return iadd
        #
        def leave_start():
            engine.say("From which date you want your leave")
            engine.runAndWait()
            print('Say you start date: ')
            res = record()
            i2 = res
            return i2
        #
        def leave_end():
            engine.say("Till which date you want your leave")
            engine.runAndWait()
            print('Say you end date: ')
            res = record()
            i3 = res
            return i3
        #
        def leave_type():
            engine.say("Which type of leave you want")
            engine.say("one E L ,two  C L , three H P L")
            engine.runAndWait()
            print('Say you leave type: ')
            res = record() 
            i4 = res
            return i4
        #
        def leave_reason():
            engine.say("Please specify the purpose of your leave")
            engine.runAndWait()
            print('Say you leave reason: ')
            res = record()
            i5 = res
            return i5
         
        '''Machine get command'''
        def main():
            res = record()
            send()
            print('orignal -- '+res)
        
            if res=='':
                print('I cannot hear you')
                engine.say("Sorry , I cannot hear you")
                engine.runAndWait()

            elif res in machine_info_list: #First command if we ask for machine information
                res = 'Get machine information'
                print(res+'\n\n')
                print('Which machine information you would like to see\n\n')
                engine.say("Which machine information you want")
                engine.runAndWait()
                res = record()
                send()
                if res in machine_cmd_all:
                    # machine_info = get_json_all()
                    machine_info = 'This is machine info'
                    statusm = 'True'
                    send_machine_info_status(machine_info,statusm)
                else:
                    final = get_json_byName()
                    find_machine(final)

            elif res in leave_app_call:
                leave_form()

                def name_confirm():
                    name = leave_name()
                    status = 'pn'
                    send_name(name,status)
                    return name

                def address_confirm():
                    address = leave_address()
                    status = 'adl'
                    send_name(address,status)
                    return address
                #
                def start_confirm():
                    start = leave_start()
                    status = 'fd'
                    send_name(start,status)
                    return start
                #
                def end_confirm():
                    end = leave_end()
                    status = 'ld'
                    send_name(end,status)
                    return end
                #
                def type_confirm():    
                    typex = leave_type()
                    status = 'lt'
                    send_name(typex,status)
                    return typex
                #
                def reason_confirm():
                    reason = leave_reason()
                    status = 'r'
                    send_name(reason,status)
                    return reason
                def leave_main():
                    name = name_confirm()
                    address = address_confirm()
                    start = start_confirm()
                    end = end_confirm()
                    typex = type_confirm() 
                    reason = reason_confirm()
                    print("Is this information correct")
                    conf = confirm()
                    if conf=='no':
                        print('Say your information again')
                        leave_main()
                    else:
                        add_pdf(name,address,start,end,typex,reason)
                        final = 'fuck'
                        status = 'over'
                        send_name(final,status)
                leave_main()
                engine.say('Your information is now saved into a PDF successfully')
                engine.runAndWait()
        # def record():
        #     global res
        #     print('Recording')
        #     CHUNK = 1024
        #     FORMAT = pyaudio.paInt16
        #     CHANNELS = 2
        #     RATE = 44100
        #     RECORD_SECONDS = 3
        #     WAVE_OUTPUT_FILENAME = "output.wav"

        #     p = pyaudio.PyAudio()

        #     stream = p.open(format=FORMAT,
        #                     channels=CHANNELS,
        #                     rate=RATE,
        #                     input=True,
        #                     frames_per_buffer=CHUNK)


        #     frames = []

        #     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        #         data = stream.read(CHUNK)
        #         frames.append(data)


        #     stream.stop_stream()
        #     stream.close()
        #     p.terminate()

        #     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        #     wf.setnchannels(CHANNELS)
        #     wf.setsampwidth(p.get_sample_size(FORMAT))
        #     wf.setframerate(RATE)
        #     wf.writeframes(b''.join(frames))
        #     wf.close()
        #     os.system('sox output.wav -c 2 -r 8000 -b 16 soxout.wav')
        #     res = os.popen('deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio /home/jidnyesh/Downloads/final/Voice-Recognition/mysite/soxout.wav').read()
        #     print('Done')
        #     lis_res = list(res)
        #     res = ''.join(lis_res[:-1])
        #     print(res)
        #     if res=='exit application':
        #         send_leaveform_status(leave_msg='False')
        #         send_reload(reloadp='True')
        #     else:
        #         return res
        def record():
            global res
            r = sr.Recognizer()  
            with sr.Microphone() as source:  
                print("Please wait. Calibrating microphone...")  
                # listen for 5 seconds and create the ambient noise energy level  
                r.adjust_for_ambient_noise(source, duration=3)
                print("Say something!")
                a = r.listen(source)
                res = r.recognize_google(a)
                print(res)
            return res
        
        main()

       
        
