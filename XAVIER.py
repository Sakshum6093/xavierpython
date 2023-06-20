import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import sys
import subprocess
import pynput
import pylint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I AM XAVIER , HOW MAY I HELP U SIR?")    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as E:
        
        print("Say that again please...")  
        return "None"
        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # WIKIPEDIA
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # YOUTUBE
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # GOOGLE
        elif 'open google' in query:
            webbrowser.open("google.com")
         
        # Thapar LMS
        elif 'open lms' in query:
                speak("opening lms honey ")
                webbrowser.open("https://ada-lms.thapar.edu/moodle/login/index.php")

        # # STACKOVERFLOW
        elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")   

        # MUSIC
        elif 'play music' in query:
            music_dir = 'D:\\MUSIC'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        # TIME 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # SHUTDOWN
        elif 'shutdown' in query:
                speak("Okay boss , have a nice day, see you later sir!")
                sys.exit() 









        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        