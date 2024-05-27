import requests
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_weather(city = 'wardha'):
    api_key = '26b9fb73dd3d5f28738f99fefd4f84b5'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        weather = weather_info
        if weather:
            speak(f"Todays weather in {city} is as follow")
            speak(f"Temperature: {weather['temperature']} Celcius")
            speak(f"Humidity: {weather['humidity']} percent")
            speak(f"Wind Speed: {weather['wind_speed']} meter per second")
            speak(f"Over all condition is {weather['description']}")
            speak('Enjoy your day')
            print(f"Weather in {city}:") 
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Error fetching weather data:", data["message"])
        speak('Sorry Prajwal, I am not getting waether information my my source')

