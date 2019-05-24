import speech_recognition as sr  
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')

name = '''
कृपया प्रतीक्षा करें, हिंदी भाषा का अनुवाद लोड हो रहा है
कई बार लोगो द्वारा यह प्रश्न पूछा जाता है कि आखिर निबंध क्या है? और निबंध की परिभाषा क्या है? वास्तव में निबंध एक प्रकार की गद्य रचना होती है। जिसे क्रमबद्ध तरीके से लिखा गया हो। एक अच्छा निबंध लिखने के लिए हमें कुछ बातों का ध्यान देना चाहिए जैसे कि – हमारे द्वारा लिखित निबंध की भाषा सरल हो, इसमें विचारों की पुनरावृत्ति ना हो, निबंध के विभिन्न हिस्सों को शीर्षकों में बांटा गया हो आदि।
'''

engine.setProperty('voices', voices[29].id)
engine.setProperty('rate', 125)
engine.say(name)
engine.runAndWait()


# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
    print("Please wait. Calibrating microphone...")  
    # listen for 5 seconds and create the ambient noise energy level  
    r.adjust_for_ambient_noise(source, duration=5)  
    print("Say something!")  
    audio = r.listen(source,timeout=8)  

# recognize speech using Sphinx  
try:  
    print("Sphinx thinks you said " + r.recognize_sphinx(audio,language='hi-IN') + "'")  
except sr.UnknownValueError:  
    print("Sphinx could not understand audio")  
except sr.RequestError as e:  
    print("Sphinx error; {0}".format(e)) 