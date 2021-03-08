import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening 👂...')
        #for index, name in enumerate(sr.Microphone.list_microphone_names()):
        #    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    print('Something went wrong')
