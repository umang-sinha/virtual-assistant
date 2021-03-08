import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hey Umang! What can I do for you?")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Listening 👂...')
        #for index, name in enumerate(sr.Microphone.list_microphone_names()):
        #    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
        else:
            print("Sorry I couldn't recognize you")
except:
    print('Something went wrong')
