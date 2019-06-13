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

# recog = [
#     'हाय आयुध',
#     'हेलो आयुध',
#     'सुनो आयुध',
#     'चुनाव आयोग',
#     'आयुष सुनो',
#     'आयुध सुनो',
#     'हाय आयोग',
#     'सुनो आयुष',
#     'सुनो आयुष',
#     'सुनवा युद्ध',
#     'सुना युद्ध',
#     'सोना युद्ध',
#     'सुनो युद्ध',
#     'सुनवाई युद्ध',
#     'ब्लू आइज',
#     'हेलो आयुष',
#     'सुनो आयोग',
#     'हाय आयुक्त',
#     'आयुध',
#     'हाय',
#     'सोनू आयोग',
# ]


# machine = [
#     'मशीन की इंफॉर्मेशन निकालो',
#     'मशीन की पूरी इंफॉर्मेशन निकालो',
#     'मशीन की इन पुणे का लो',
#     'मशीन की इन्फॉर्म कालो',
#     'मशीन का डाटा बताओ',
#     'मशीन का डाटा निकालो',
#     'मशीन की इंफॉर्मेशन दिखाओ',
#     'मशीन के इंफॉर्मेशन दिखाओ',
#     'मशीन की इंफॉर्मेशन निकालो',
# ]

# machine_name_select = [
#     'sub machine ka data dikhao',
#     'sab',
#     'sub',
#     'sab machine ka data dikhao',
#     'sab sab'
# ]

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
        # message = event['message']
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
        # os.system('sox output.wav -c 2 -r 16000 -b 16 soxout.wav')
        output = os.popen('deepspeech --model /home/jidnyesh/Downloads/models/output_graph.pbmm --alphabet /home/jidnyesh/Downloads/models/alphabet.txt --lm /home/jidnyesh/Downloads/models/lm.binary --trie /home/jidnyesh/Downloads/models/trie --audio /home/jidnyesh/Downloads/Voice-recog/Voice-Recognition/test/mysite/output.wav').read()
        print('Done')
        print(output)
        res = output
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': res,
            # 'response':res_back,
        }))
