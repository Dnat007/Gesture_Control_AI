import pyttsx3 #pip install pyttsx3
import pywhatkit
import speech_recognition as sr #pip install speechRecognition
import datetime
import Alarm_Code.Alarmcode # import alarm
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import Web_Scraping.weather


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<15:
        speak("Good Afternoon!")

    elif hour>=15 and hour<18:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    #it will speak at the starting of the program so it sounds good.
    speak("I am Shreya Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhisingh208b@gmail.com', 'abhidadag')
    server.sendmail('abhisingh208b@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what do you mean by' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")

        elif "open c compiler" in query:
            webbrowser.open("https://www.onlinegdb.com/online_c_compiler")

        elif "open java compiler" in query:
            webbrowser.open("https://www.onlinegdb.com/online_java_compiler")

        elif "open python compiler" in query:
            webbrowser.open("https://www.onlinegdb.com/online_python_compiler")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")

        elif "open my mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "send an email" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")

        elif "open college mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

        elif 'alarm' in query:
            Alarm_Code.Alarm_code_voice.alarm()

        elif 'weather' in query:
            Web_Scraping.weather.weather()

        elif 'play music' in query:
            music_dir = 'C:\\pics\\Asongs'
            songs = os.listdir(music_dir)
            print(songs)
            # we have 30 songs so we can choose a number between 0 - 29 to play what song we like
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play' in query:
            command_from_us = query.replace('play', '')
            speak('playing' + command_from_us)
            # playonyt -->> play on youtube
            pywhatkit.playonyt(command_from_us)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S %p") #%p is for am and pm
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Asus\\PycharmProjects\\Gesture_Control_AI\\AI"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            pycharm ="C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains Toolbox\\PyCharm Professional"

        elif 'open command prompt' in query:
            location = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os.startfile(location)

        elif 'open run' in query:
            run = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run"
            os.startfile(run)

        elif 'open control panel' in query:
            control = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
            os.startfile(control)

        # elif 'open my computer' in query:
        #     pc = "C:\\Users\\Asus\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\This PC"
        #     os.startfile(pc)

        elif 'are you single' in query:
             speak('sorry, I am already mingle with asus TUF but i can be your friends forever')

        elif 'do you love me' in query:
             speak('I already told you that i love someone but for you i can be your freinds with benifit')

        elif 'who are you' in query:
             speak('I m an Artificial Intelligence which helps you in those moment where you could not find the solutions  ')

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arvindsingh611e@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend abhishek. I am not able to send this email")
