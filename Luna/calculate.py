import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def calculate(query):
    query = query.replace('into',"*").replace('multiply',"*").replace('divide',"/").replace('plus',"+").replace('minus','-')
    if '*' in query:
        result = eval(query)
        print(f'{query}={result}')
        speak(result)
    elif '/' in query:
        result = eval(query)
        print(f'{query}={result}')
        speak(result)
    elif '+' in query:
        result = eval(query)
        print(f'{query}={result}')
        speak(result)
    elif '-' in query:
        result = eval(query)
        print(f'{query}={result}')
        speak(result)
    else:
        speak('Invalid expression')
        print('Invalid expression')
        
              