import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hi! I am Alexa, your virtual assistant. What can I do for you?")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            # for index, name in enumerate(sr.Microphone.list_microphone_names()):
            #    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
            print('Listening 👂...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        command = ''
        engine.say('Sorry something went wrong')
    return command


def run_assistant():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print('The time is ' + time)
        talk('The time is ' + time)


run_assistant()
