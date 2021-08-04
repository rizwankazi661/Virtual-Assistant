import pyttsx3                                          #pip install pyttsx3   #It is a library for text to speech
import speech_recognition as sr                         #pip install speechRecognition  #This class provides access to the speech recognition service. This service allows access to the speech recognizer.
import datetime
import wikipedia                                        #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import pyautogui
import time

engine = pyttsx3.init('sapi5')                          #Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Friday at your Service.")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')                     #Using google for voice recognition.
        print(f"User said: {query}\n")                                          #User query will be printed.

    except Exception as e:    
        print("Say that again please...")
        speak('Say that again please...')  
        return "None"
    return query

if __name__ == "__main__":
    array=['I am good Sir' , 'None of your buisness' , ' I am fine   Thank you for asking ' , ' I wont say that ']
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            o="Opening youtube please wait"
            print(o)
            speak(o)
            webbrowser.open("youtube.com")
            time.sleep(10)
            pyautogui.click(769,144)
            sc="what should i search sir ?"
            print(sc)
            speak(sc)
            txt=takeCommand()
            search="searching",txt
            print(search)
            speak(search)
            pyautogui.typewrite(txt)
            time.sleep(2)
            pyautogui.typewrite("\n")
            
        elif 'open google' in query:
            o="opening google for you sir please wait for a second"
            print(o)
            speak(o)
            webbrowser.open("google.com")
            time.sleep(10)
            sc="what should i search sir ?"
            print(sc)
            speak(sc)
            txt=takeCommand()
            search="searching",txt
            print(search)
            speak(search)
            pyautogui.typewrite(txt)
            time.sleep(2)
            pyautogui.typewrite("\n")
            

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open movies folder' in query:
            codePath = "E:\Movies"
            os.startfile(codePath)

        elif'tell me about yourself' in query:
            speak('My  name  is  Friday  i  am  a  AI  bot  created  by  Rizwan Zahidali  Kazi  on  26  may  2021')

        elif'how are you' in query:
            speak(random.choice(array))

        elif'send message through whatsapp' in query:
            w="Opening whatsapp please wait rizwan"
            webbrowser.open("https://web.whatsapp.com/")
            print(w)
            speak(w)
            time.sleep(8)
            pyautogui.click(222,281)
            time.sleep(1)
            q1="whom do you want to message and trouble"
            print(q1)
            speak(q1)
            time.sleep(1)
            cname=takeCommand()
            makesure="are you satisfied with this name pronountiation ",cname
            speak(makesure)
            makesure=takeCommand()
            time.sleep(1)
            if 'yes' in makesure:
                sm="sending message to ",cname
                print(sm)
                speak(sm)
                pyautogui.typewrite(cname)
                time.sleep(1)
                pyautogui.click(273,425)
                mess="Sir please tell the message"
                print(mess)
                speak(mess)
                m=takeCommand()
                time.sleep(2)
                pyautogui.typewrite(m)
                pyautogui.typewrite("\n")
                break
            elif 'no' in makesure:
                cancel="Cancelling the message transfer "
                print(cancel)
                speak(cancel)
                break
        elif 'video call through whatsapp' in query:
            w="Opening whatsapp please wait rizwan"
            webbrowser.open("https://web.whatsapp.com/")
            print(w)
            speak(w)
            time.sleep(8)
            pyautogui.click(222,281)
            time.sleep(1)
            a="Whose face do you want to see in a video call ?"
            print(a)
            speak(a)
            b=takeCommand()

        elif'open word' in query:
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)

        elif'chrome' in query:
            path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            time.sleep(1)
            wto="What do you want me to do?"
            print(wto)
            speak(wto)
            wto=takeCommand()
            time.sleep(4)
            if 'ERP' in wto:
                pyautogui.typewrite("https://student.alliance.edu.in/KnowledgePro/StudentLogin.do")
                pyautogui.typewrite("\n")
                time.sleep(4)
                pyautogui.click(864,751)
                time.sleep(1)
                captha="Please say me the text given in the box"
                print(captha)
                speak(captha)
                captha=takeCommand().lower()
                captha=captha.replace(" ","")
                print(captha)
                pyautogui.typewrite(captha)
                pyautogui.typewrite("\n")
                time.sleep(5)
                #print(pyautogui.position())
                pyautogui.click(1285,645)

            elif 'open Outlook' in wto:
                pyautogui.typewrite("https://outlook.office.com/mail/inbox")
                pyautogui.typewrite("\n")
                new_task="What is the new task ?"
                print(new_task)
                speak(new_task)
                new_task=takeCommand()
                #pyautogui.click(864,751)

        elif 'type' in query:
            speak('Say the sentences')
            time.sleep(2)
            typo=takeCommand()
            while (typo != 'exit'):
                pyautogui.typewrite(typo)
                pyautogui.typewrite(" ")
                typo=takeCommand()

        elif'exit' in query:
            s="Hope i was able to do all the work you said me to do"
            print(s)
            speak(s)
            q="are you sure you want to shut me down?"
            print(q)
            speak(q)
            q=takeCommand()
            if 'yes' in q:
                speak("Friday shutting down")
                exit()
            elif 'no' in q:
               a="ok sir please continue troubling me :"
            print(a)
            speak(a)
            