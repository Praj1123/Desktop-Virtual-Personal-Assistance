import pyttsx3
import pygame
import speech_recognition
import bs4
import datetime
import random
import pyautogui

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
    pygame.mixer.music.load("VPA/audio.mp3")
    pygame.mixer.music.play()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listining...")
        play_audio()
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said {query.lower()}")
    except Exception as e:
        print("Speak Again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up luna" in query:
            from greetMe import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                print(query)
                count = 0
                if query == "none":
                    count = count + 1
                if "none" in query and count == 5:
                    break
                if "sleep luna" in query:
                    speak("Ok Sir, Wake me up anytime")
                    break
                elif "hello luna" in query:
                    speak("Hello prajwal,how are you")
                elif "i am fine" in query:
                    speak("that's greate prajwal,how can i help you")

                elif "play" in query and "on youtube" in query:
                    from search import play_command_on_Youtube

                    speak("Alright")
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
                    searchGoogle(query)

                elif "wikipedia" in query:
                    from search import searchWekepedia

                    speak("Alright")
                    searchWekepedia(query)

                elif "weather" in query:
                    from weather import get_weather

                    get_weather()

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Its {strTime}")

                elif "date" in query:
                    strDate = datetime.datetime.now().strftime("%d/%m/%Y")
                    speak(f"Todays date is {strDate}")

                elif "switch off" in query:
                    speak(
                        "Ok prajwal,When ever you need my help,just call me out,have a nice day,Buy"
                    )
                    exit()

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
                        file = open("VPA/songs.txt", "r")
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
                    press_keys("k")
                    speak("Pausing the video")

                elif "play" in query:
                    press_keys("k")
                    speak("Resuming the video")
                    video_paused = False

                elif "skip" in query:
                    press_keys("s")
                    speak("Skipping the ad")

                elif "increase volume" in query:
                    for _ in range(5):
                        press_keys("up")

                elif "decrease volume" in query:
                    for _ in range(5):
                        press_keys("down")

                elif "fast forward" in query:
                    for _ in range(5):
                        press_keys("right")

                elif "rewind" in query:
                    for _ in range(5):
                        press_keys("left")

                elif "today's headline" in query:
                    speak(
                        "ok, what would you like to here, top headlines of india or world"
                    )
                    input = input("Type india or world:")
                    from news import news

                    pyautogui.press("enter")

                elif "send whatsapp message" in query:
                    speak("Enter the receiver number: ")
                    number = int(input("Enter the receiver number: "))
                    speak("Enter the message: ")
                    message = input("Enter the message: ")
                    speak("Specify timeing 24 hr  (hour): ")
                    hr = int(input("Specify timeing 24 hr  (hour): "))
                    speak("Specify timeing 24 hr format (minute): ")
                    mn = int(input("Specify timeing 24 hr format (minute): "))
                    from whatsapp import send
                    send(number, message, hr, mn)

                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("luna", "")
                    speak("Opening" + query)
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press('enter')
