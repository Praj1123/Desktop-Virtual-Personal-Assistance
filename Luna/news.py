import response
import json
import pyttsx3
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def todays_headline_india():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=d5ad4cc0d4c44f449c0c78891ec67fc6'
    news = requests.get(url).text
    news = json.loads(news)
    articals = news['articles']
    speak('here are top headlines in india')
    for artical in articals:
        title = artical['title']
        print(title)
        speak(title) 

def todays_headline_world():
    url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d5ad4cc0d4c44f449c0c78891ec67fc6'
    news = requests.get(url).text
    news = json.loads(news)
    articals = news['articles']
    speak('here are top headlines in world')
    for artical in articals:
        title = artical['title']
        print(title)
        speak(title) 
        
def news(query):
    if query=='india':
        todays_headline_india()
    elif query=='world':
        todays_headline_world()  
    else:
        speak('Sorry prajwal, I could not complete your request')  
    