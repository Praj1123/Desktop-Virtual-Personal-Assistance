import time
import datetime
import pyttsx3
import pygame
import subprocess
from time import sleep
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def play_audio():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('VPA/alarm.mp3')
    pygame.mixer.music.play()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def check_alarm():
    while True:
        file = open('VPA/alarmdb.txt', 'r+')
        data = file.readlines()
        file.seek(0)  # Move the file cursor to the beginning
        current_time = datetime.datetime.now().strftime('%H:%M')
        lst_of_time = [item.strip() for item in data]  # Remove newline characters

        # Check if all alarms are 'None'
        if all(time == 'None' for time in lst_of_time):
            file.close()
            print("All alarms are None. Stopping the loop.")
            break

        for i in range(len(lst_of_time)):
            if current_time == lst_of_time[i]:
                play_audio()
                lst_of_time[i] = 'None'
                data[i] = 'None\n'
                file.truncate(0)  # Clear the file content
                file.writelines(data)  # Write the updated data to the file
                print('Alarm executing...')
                break  # Exit loop once alarm is found and executed

        file.close()
        sleep(5)

def setAlarm(time):
    file = open('VPA/alarmdb.txt', 'a')
    file.write(time + '\n')
    file.close()
    speak("Alarm set successfully")


alarm_thread = threading.Thread(target=check_alarm)
alarm_thread.start()
print('Thread is running...')


    
