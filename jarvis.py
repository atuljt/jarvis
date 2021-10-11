import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser

import wikipedia
from selenium import webdriver


r = sr.Recognizer()
engine = pyttsx3.init("sapi5")

"VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)#changing index, changes voices. 0 for male

"""VOLUME"""
engine.setProperty('volume',5)    # setting up volume level  between 0 and 1

def talk(txt):
    engine.say(txt)
    engine.runAndWait()



def intro():
    currentTime = datetime.datetime.now()
    currentTime.hour
    hello=engine.say("hello")
    if currentTime.hour < 12:
        engine.say('Good morning sir')
    elif 12 <= currentTime.hour < 18:
        engine.say('Good afternoon sir')
    else:
        engine.say('Good evening sir . mam')
    engine.say("I am jarvis . And how may i help you ")
    engine.runAndWait()
intro()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.... ")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            command = command.lower()
            print("You say:",command)
            return command

    except:
        pass



def run_jarvis():
    command=take_command()
    if 'wikipedia' in command:
        talk('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif "stop" in command:
        talk("thankyou sir . have a nice day ")
        quit()

    elif "who are you" in command:
        talk(intro())

    elif "hello" in command:
        talk("hello sir i am jarvis")

    # elif "developed" or "develop" in command:
    #     talk(" i am developed by atul sharma")

    elif 'open google' in command:
        talk("opening google.com")
        webbrowser.open("google.com")

    elif 'open youtube' in command:
        talk("opening youtube.com")
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        talk("google.com")
        webbrowser.open("google.com")

    else:
        talk('Please say the command again.')

while True:
    run_jarvis()
