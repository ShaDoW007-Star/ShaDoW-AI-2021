import speech_recognition as sr
import datetime
import pyttsx3
import os
import random
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <= 12:
        speak("Good Morning..shadow")
    elif hour > 12 and hour <= 18:
        speak("good afternoon..shadow")
    elif hour > 18 and hour <= 23:
        speak("good evening..shadow")
    else:
        speak("good night..shadow")


def talk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Aryan said : {query}")

    except Exception as e:
        print(e)
        print("please say that again...")
        return "None"
    return query


if __name__ == '__main__':
    greeting()
    speak("how are you...tell me what can i do for you")
    while True:
        query = talk().lower()

        if 'song' in query:
            directory = "D:\\song\\UTTRAYAN SONGS"
            song = os.listdir(directory)
            os.startfile(os.path.join(directory, random.choice(song)))

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")