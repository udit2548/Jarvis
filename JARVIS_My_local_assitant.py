# This code repository simulates virtual assistants like google,alexa and siri etc.
# Required modules and packages.
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

# Speak function enables assistant to speak and communicate with user.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# wishMe function will greet user and welcome him.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak('Hi, This is Jarvis.How may I help You?')

# takeCommand function will take input from the user and recognises it and returns the string output.
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold=800
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Say that again please ...')
        return "None"
    return query

# This function will send email .
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('assistantjarvis45@gmail.com','jarvisassistant')
    server.sendmail('assistantjarvis45@gmail.com',to,content)
    server.close()

# Main function
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'time' in query:
            # This will tell the current time.
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open python interpreter' in query:
            # Provide similar directory for your pc in order to open any code-editor.
            codepath = "C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnk"
            os.startfile(codepath)

        elif 'open notepad' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to="uditarora06@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Due to some issue, I am unable to send e-mail at the moment')

        elif 'stop ' in query:
            exit()
