import pyttsx3
import pygame
import speech_recognition
import bs4
import datetime
import random
import pyautogui
import time
import os
import eel

eel.init("Luna/font_end/interface")

@eel.expose
def play_booting_audio():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Luna/font_end\multimedia/start_audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    return "success"


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def play_audio():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Luna/font_end\multimedia/audio.mp3")
    pygame.mixer.music.play()


def takeCommand1():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listining...")
        eel.update("Listening")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        eel.update("Understanding")
        query = r.recognize_google(audio, language="en-in")
        eel.update(f"You said: {query.lower()}")
        print(f"you said {query.lower()}")
    except Exception as e:
        print("Speak Again")
        eel.update("Speak_Again")
        return "None"
    return query


def takeCommand2():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listining...")
        eel.update("Listening")
        play_audio()
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        eel.update("Understanding")
        query = r.recognize_google(audio, language="en-in")
        eel.update(f"You said: {query.lower()}")
        print(f"you said {query.lower()}")
    except Exception as e:
        print("Speak Again")
        eel.update("Speak_Again")
        return "None"
    return query


@eel.expose
def run():
    import pyttsx3
    import pygame
    import speech_recognition
    import bs4
    import datetime
    import random
    import pyautogui
    import time
    import os
    import eel

    play_audio()
    while True:
        query = takeCommand1().lower()
        if "wake up luna" in query:
            from greetMe import greetMe

            greetMe()
            count = 0
            while True:
                query = takeCommand2().lower()
                print(query)
                if query == "none" or query == None:
                    count = count + 1
                    continue
                if query != "none" or query == None:
                    count = 0
                if (query == "none" or query == None) and count == 5:
                    speak("Going to sleep, wake me up any time")
                    break
                if "sleep luna" in query:
                    speak("Ok Sir, Wake me up anytime")
                    break
                if "switch off luna" in query:
                    speak("Ok Sir, Shutting down")
                    exit()

                elif "hello luna" in query:
                    speak("Hello prajwal,how are you")

                elif "i am fine" in query:
                    speak("that's great prajwal,how can i help you")

                elif "play" in query and "on youtube" in query:
                    from search import play_command_on_Youtube

                    speak("Opening youtube")
                    play_command_on_Youtube(query)

                elif "set an alarm" in query:
                    speak("Ok,tell the time to set")
                    print("Time should in this format (HH:MM:)")
                    time = input("Enter time : ")
                    from setAlarm import setAlarm
                    setAlarm(time)

                elif "google" in query:
                    from search import searchGoogle

                    speak("Alright")
                    query = (
                        query.replace("google", "")
                        .replace("on", "")
                        .replace("search", "")
                        .replace("luna", "")
                    )
                    searchGoogle(query)

                elif "wikipedia" in query:
                    from search import searchWekepedia

                    speak("Alright")
                    query = (
                        query.replace("wikipedia", "")
                        .replace("on", "")
                        .replace("search", "")
                        .replace("luna", "")
                    )
                    searchWekepedia(query)

                elif "weather" in query:
                    from weather import get_weather

                    speak("wait...")
                    get_weather()

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Its {strTime}")

                elif "date" in query:
                    strDate = datetime.datetime.now().strftime("%d/%m/%Y")
                    speak(f"Todays date is {strDate}")

                elif "remember that" in query:
                    query = query.replace("remember that", "").replace("luna", "")
                    from remember_function import remember

                    remember(query)

                elif "what do you remember" in query:
                    from remember_function import what_remember

                    what_remember(query)

                elif "i am tired" in query:
                    speak("ok , let me enterten you, playing your favourite song")
                    try:
                        file = open("Luna\songs.txt", "r")
                        songs = file.readlines()
                        file.close()
                        song = random.choice(songs)
                        from search import play_command_on_Youtube

                        play_command_on_Youtube(song)
                    except Exception as e:
                        speak("I have some problem with the task , sorry")
                        print(e)

                elif "close" in query:
                    speak("Closing...")
                    pyautogui.hotkey("alt", "f4")

                elif "pause" in query:
                    speak("Pausing the video")
                    pyautogui.press("k")

                elif "play" in query:
                    speak("Resuming the video")
                    pyautogui.press("k")

                elif "skip" in query:
                    speak("Skipping the ad")
                    pyautogui.press("k")

                elif "increase volume" in query:
                    for _ in range(5):
                        pyautogui.press("up")

                elif "decrease volume" in query:
                    for _ in range(5):
                        pyautogui.press("down")

                elif "fast forward" in query:
                    for _ in range(5):
                        pyautogui.press("right")

                elif "rewind" in query:
                    for _ in range(5):
                        pyautogui.press("left")

                elif "today's headlines" in query:
                    speak(
                        "ok, what would you like to here, top headlines of india or world"
                    )
                    ans = takeCommand2()
                    from news import news

                    news(ans)
                elif "open whatsapp" in query:
                    query = query.replace("open whatsapp", "")
                    query = query.replace("lune", "")
                    pyautogui.press("super")
                    time.sleep(1)
                    pyautogui.typewrite("whatsapp")
                    time.sleep(2)
                    pyautogui.press("enter")
                    speak("opened")
                    recall = ""
                    while True:
                        query = takeCommand()
                        if "search" in query:
                            query = query.replace("search", "")
                            query = query.replace("luna", "")
                            pyautogui.hotkey("ctrl", "f")
                            pyautogui.hotkey("ctrl", "a")
                            pyautogui.press("delete")
                            pyautogui.typewrite(query)
                            time.sleep(1)
                            pyautogui.press("tab")
                            pyautogui.press("enter")
                            speak("chat opened")
                            continue
                        elif "type" in query:
                            query = query.replace("type", "")
                            query = query.replace("luna", "")
                            query = query.replace("send", "")
                            query = query.replace("and", "")
                            pyautogui.hotkey("ctrl", "a")
                            pyautogui.press("delete")
                            pyautogui.typewrite(query)
                            speak(f"typing {query}")
                            continue
                        elif "post" or "send" in query:
                            pyautogui.press("enter")
                            speak("send")
                            continue
                        elif "close" in query:
                            pyautogui.hotkey("alt", "f4")
                            speak("closed")
                            break

                elif "open" in query:
                    print("open")
                    query = query.replace("open", "")
                    query = query.replace("luna", "")
                    speak("Opening" + query)
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")
                else:
                    speak("ok, wait for a response")
                    from bot import chatBot

                    query = query.replace("luna", "")
                    response = chatBot(query)
                    eel.response(response)
                    speak(response)

        elif "switch off luna" in query:
            speak("Ok, shutting down, goodby")
            break

eel.start("index.html")
