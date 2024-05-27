import win32com.client
import speech_recognition as sr
import pywhatkit
import pyautogui
import keyboard
import pygame
import subprocess

# Function to convert text to speech
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
    
def play_audio():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('VPA/audio.mp3')
    pygame.mixer.music.play()
    
def open_whatsapp(application_path):
    try:
        subprocess.Popen(application_path)
        print(f"Opened {application_path} successfully.")
        say('Opening Whatsapp')
    except Exception as e:
        print(f"Error opening {application_path}: {e}")

# Function to recognize speech input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        play_audio()
        print("Listening...")
        try:
            r.pause_threshold = 0.8
            audio = r.listen(source)
            query = r.recognize_google(audio)
            print("You said:", query)
            say(query)
            return query
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
            say("Sorry, I could not understand what you said")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(
                    e
                )
            )
            say("Sorry, there was an error processing your request")
        except Exception as e:
            print("Error:", e)
            say("Sorry, there was an error")
        return None


# press key
def press_keys(keys):
    for key in keys:
        pyautogui.press(key)


# Function to play command on YouTube
def play_command_on_Youtube(command):
    command = command.replace("play", "").replace("on youtube", "")
    say("Playing " + command)
    pywhatkit.playonyt(command)
    video_paused = False

    while True:
        command = takeCommand()
        if command is None:
            continue

        if 'close youtube' in command.lower():
            press_keys('k')
            say("Closing Youtube")
            break

        if "pause" in command.lower():
            if not video_paused:
                press_keys('k')  # Press 'k' key to toggle play/pause
                say("Pausing the video")
                video_paused = True
            else:
                say("The video is already paused")

        if "play" in command.lower():
            if video_paused:
                press_keys('k')  # Press 'k' key to toggle play/pause
                say("Resuming the video")
                video_paused = False
            else:
                say("The video is already playing")

        if "skip" in command.lower():  # Corrected command to "skip ads"
            press_keys('s')  # Press 's' key to skip ad
            say("Skipping the ad")

        if "increase volume" in command.lower():
            for _ in range(5):  # Press 'up arrow' key 5 times to increase volume
                press_keys('up')

        if "decrease volume" in command.lower():  # Added command for decreasing volume
            for _ in range(5):  # Press 'down arrow' key 5 times to decrease volume
                press_keys('down')

        if "fast forward" in command.lower():
            for _ in range(5):  # Press 'right arrow' key 5 times to fast forward
                press_keys('right')

        if "rewind" in command.lower():  # Corrected typo in "rewind"
            for _ in range(5):  # Press 'left arrow' key 5 times to rewind
                press_keys('left')



if __name__ == "__main__":
    say("This is Luna")
    say("Your Desktop assistant. How can I help you?")

    while True:
        command = takeCommand()
        
        if command is None:
            continue

        if 'exit' in command.lower():
            break

        if "play" in command.lower() and "on youtube" in command.lower():
            play_command_on_Youtube(command)
        
