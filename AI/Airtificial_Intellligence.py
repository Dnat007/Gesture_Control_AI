import datetime

import pyjokes
# for our talk to AI
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

# for the understanding
listener = sr.Recognizer()
# for our talk to AI
engine = pyttsx3.init()
# for giving it to all that voice which python library can suppport
voices = engine.getProperty('voices')
# for the change in voice
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        # for listening
        with sr.Microphone() as source:
            print('Start speaking!!')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'amit' in command:
                command = command.replace('amit', '')
    #                print(command)
    except:
        pass
    return command


def run_amit():
    command = take_command()
    print(command)
    # working of Ai
    if 'play' in command:
        command_from_us = command.replace('play', '')
        talk('playing' + command_from_us)
        # playonyt -->> play on youtube
        pywhatkit.playonyt(command_from_us)

    elif 'time' in command:
        # get time in perfect string
        #  %p for am and pm
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        information = command.replace('who is', '')
        info = wikipedia.summary(information, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('sorry, I am already mingle with  ')
    elif 'do you love me' in command:
        talk('i already love you thats why i m with you but i have 4')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')


while True:
    run_amit()
