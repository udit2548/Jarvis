# Jarvis
Jarvis is a virtual assistant like Siri and Alexa which I had tried to simulate the same using Python Programmming Language.
This assitant recognises speech input and convertes it into string output.

Various Features and tasks performed by this assistant is:

1. Like it first wishes and greet the user.
2. It can retreive the information from Wikipedia.
3. It can open Google for you.
4. It can open Youtube for you.
5. It can open Python Interpreter(IDLE),Notepad for you.
6. It can open Stackoverflow for you.
7. It can open Instagram,Faccebook for you.
8. It can open code editor like Vs-Code,Code-Blocks etc of your choice.
9. It can report current time to the user.
10. It can send Email to the intended user for you.

You have to install following Python Modules to run the code in your Local Machine:
1. pyttsx3 (pip install pyttsx3)
2. speech_recognition (pip install SpeechRecognition)
3. wikipedia (pip intstall wikipedia)
4. webbrowser (pip install webbrowser) 
5. smtplib,datetime and os are inbuilt packages so no need to install it.

Note: 1. To open code editor of your choice and python interpreter(IDLE) you have to provide
path of your local directories in the source code to avoid error.
2. If there is any error regarding microphone or related to pyttsx3 or speech_recognition module do follow this step:
    pip install pipwin
    then run this command
    pip install PyAudio
