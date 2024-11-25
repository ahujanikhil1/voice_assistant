import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        recognizer.adjust_for_ambient_noise(source)#noise cancellation
        audio= recognizer.listen(source)
        try:
            print("recognizing")
            data= recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" not understanding....")

def speechtxt(x):#pyttsx3
    a= pyttsx3.init()
    #properties
    voices= a.getProperty("voices")
    a.setProperty('voice',voices[0].id)
    rate=a.getProperty('rate')
    a.setProperty('rate',150)
    a.say(x)
    a.runAndWait()

if __name__ =='__main__':
    
        
    if "ok nikhil" in sptext().lower():
        
        while True:
                data1=sptext().lower()

                if "your name" in data1:
                    name='my name is Nikhil'
                    speechtxt(name)
                elif "your age" in data1:
                    age="my age is 21 years"
                    speechtxt(age)
                elif 'time' in data1:
                    time= datetime.datetime.now().strftime("%I%M%p")
                    speechtxt(time)
                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")
                elif 'channel' in data1:
                    webbrowser.open("https://www.youtube.com/@MagicalMomentsbyjai")

                elif "joke" in data1:
                    joke_1= pyjokes.get_joke(language="en",category='neutral')
                    print(joke_1)
                    speechtxt(joke_1)
                elif " exit" in data1:
                    speechtxt("thank you")
                    break
                time.sleep(20)
    else:
        
        print("thanks")
            
        
        



    
#speechtxt("hello my name is nikhil")
#sptext()
