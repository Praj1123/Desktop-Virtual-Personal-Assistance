import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def remember(query):
    try:
        query = query.replace('i','you')
        file = open('VPA/remember.txt','a')
        file.write(query+'\n')
        speak('remembered')
        file.close()
    except Exception as e:
        speak("I have some problem with the task,sorry for that")
        print(e)
        
def what_remember(query):
    try:
        file = open('VPA/remember.txt','r')
        data = file.read()
        file.close()
        speak('you told me to remember folling task:'+ data)
    except Exception as e:
        speak("I have some problem with the task,sorry")
        print(e)
        
            