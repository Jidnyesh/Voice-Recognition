import speech_recognition as rs
import pyaudio
import audioop
import os
import math
from os import system
import threading

# Microphone stream config.
CHUNK = 1024  # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
THRESHOLD = 1500  # The threshold intensity that defines silence
                  # and noise signal (an int. lower than THRESHOLD is silence).

SILENCE_LIMIT = 1  # Silence limit in seconds. The max ammount of seconds where
                   # only silence is recorded. When this time passes the
                   # recording finishes and the file is delivered.
        
def audio_int(num_samples=50):
    """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
    """
        
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4))) 
              for x in range(num_samples)] 
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    print(" Average audio intensity is ", r)
    stream.close()
    p.terminate()
    
    if r > THRESHOLD:
        listen(0)
    
    threading.Timer(SILENCE_LIMIT, audio_int).start()
    
def listen(x):
    r=rs.Recognizer()
    if x == 0:
        print('say Hi. How can I help?')
    with rs.Microphone() as source:
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        y = process(text.lower())
        return(y)
    except:
        if x == 1:
            print('say Good Bye!')
        else:
            print('say I did not get that. Please say again.')
            listen(1)

def process(text):
    print(text)
 #   ''''''''''''''''''''''''''''''''''''''''''''''''
 #   '''''''Your application goes here ''''''''''''''
 #   ''''''''''''''''''''''''''''''''''''''''''''''''


audio_int()