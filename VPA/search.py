import pyttsx3
import pyautogui
import pywhatkit
import win32com.client
import speech_recognition
import wikipedia
import pygame

def press_keys(keys):
    for key in keys:
        pyautogui.press(key)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def play_audio():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('VPA/audio.mp3')
    pygame.mixer.music.play()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listining...')
        play_audio()
        r.pause_threshold = 1
        r.energy_threshold  = 300
        audio = r.listen(source,0,4)
    try:
        print('Understanding...')
        query = r.recognize_google(audio,language='en-in')
        print(f'you said {query}')
    except Exception as e:
        print('Speak Again')
        return 'None'
    return query 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def play_command_on_Youtube(command):
    command = command.replace("play", "").replace("on youtube", "")
    speak("Playing " + command)
    pywhatkit.playonyt(command)

def searchGoogle(query):
    try:
        result = pywhatkit.info(query, lines=4)
        speak('This is what I found on Google: ' + result)
        print(result)
    except pywhatkit.exceptions.WikipediaException:
        speak('No information found on Google for the given query.')
    except Exception as e:
        speak('An error occurred: ' + str(e))
        
        
        
def searchWikipedia(query):
    try:
        if 'wikipedia' in query:
            # Removing unnecessary words from the query
            query = query.replace('wikipedia', '').replace('on', '').replace('search', '').replace('luna', '')
            print('This is what I found on Wikipedia:')
            result = wikipedia.page(query)
            speak(f'According to Wikipedia:{result}')
            print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print('Multiple options found. Please be more specific.')
        speak('Multiple options found. Please be more specific.')
    except wikipedia.exceptions.PageError:
        print('The page does not exist. Please try another query.')
        speak('The page does not exist. Please try another query.')
    except Exception as e:
        print('An error occurred: ' + str(e))
        speak('An error occurred: ' + str(e))
              