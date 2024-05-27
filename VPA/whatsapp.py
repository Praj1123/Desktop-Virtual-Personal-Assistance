import pywhatkit
import pyttsx3
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send_message(number, message, hr, mn):
    try:
        pywhatkit.sendwhatmsg(number, message, hr, mn)
        speak('Message sent!')
    except Exception as e:
        speak('I encountered some problem while sending the message, sorry')
        print(e)

def send(number, message, hr, mn):
    # Create a new thread with the target function and arguments
    message_thread = threading.Thread(target=send_message, args=(number, message, hr, mn))
    message_thread.start()
    print('Thread is running...')
    speak('I will send this message at the specified timing, for sure')

# Example usage
#send("+911234567890", "Hello, this is a test message!", 12, 30)
