import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {'command prompt':'cmd','paint':'paint','word':'winword','excel':'excel','chrome':'chrome','vs code':'code','powerpoint':'powerpnt'}

def openappweb(query):
    speak('Launching, wait...')
    if '.com' in query or '.in' in query or '.org' in query:
        query = query.replace('luna','').replace('open','').replace('launch','').replace(' ','')
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app_name in keys:
            if app_name in query:
                os.system(f'start {dictapp[app_name]}')
                break
        
def closeappweb(query):
    speak('Closing...')
    if 'one tab' in query or "1 tab" in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak('All tabs are closed')
    elif 'two tab' in query or '2 tab' in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak("all tabs are closed")
    elif 'three tab' in query or '3 tab' in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak("all tabs are closed")
    elif 'four tab' in query or '4 tab' in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak("all tabs are closed")
    elif 'five tab' in query or '5 tab' in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak("all tabs are closed")
    elif 'six tab' in query or '6 tab' in query:
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')
        sleep(0.5)
        speak("all tabs are closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f'taskkill /f /im {dictapp[app]}.exe')
                break