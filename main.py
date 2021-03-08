import source as source
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hi! I am Alexa, your virtual assistant. What can I do for you?")
engine.runAndWait()

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
    print('Something went wrong')
