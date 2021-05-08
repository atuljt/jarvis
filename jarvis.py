import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser
import sys
import wikipedia
from selenium import webdriver


r = sr.Recognizer()
engine = pyttsx3.init("sapi5")

"VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)#changing index, changes voices. 0 for male

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
        engine.say('Good evening sir')
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

    elif "play" in command:
        import time
        song = command.replace('play', '')
        talk("playing song on youtube"+song)
        driver = webdriver.Chrome(executable_path="A:\python\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.youtube.com/")
        time.sleep(4)
        search=driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
        search_b=driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button")
        search.send_keys(song)
        time.sleep(2)
        search_b.click()
        talk("select song you want to play. enjoy the world of music")
        time.sleep(1000)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif "stop" in command:
        talk("thankyou sir . have a nice day ")
        sys.exit()

    elif "who are you" in command:
        talk(intro())

    elif "hello" in command:
        talk("hello sir i am jarvis")

    elif "developed" in command:
        talk(" i am developed by atul sharma")

    elif "develop" in command:
        talk("i am developed by atul sharma")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    else:
        talk('Please say the command again.')

while True:
    run_jarvis()