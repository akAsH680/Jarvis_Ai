import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from PIL import Image

listener = sr.Recognizer()
engine = pyttsx3.init()

# Load the avatar image
avatar_image = Image.open("Jarvis.png")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def display_avatar():
    avatar_image.show()

def run_jarvis():
    display_avatar()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('I am in a relationship with the internet')
    elif 'how are you' in command:
        talk('I am good, how are you?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'make me laugh' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry, I could not understand. Can you say that again?')

while True:
    run_jarvis()
