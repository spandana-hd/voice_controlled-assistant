import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}\n")
    except:
        speak("Sorry, I did not understand that.")
        return ""
    return command.lower()

def process_command(command):
    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "time" in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    else:
        speak("Sorry, I don't know that yet.")

if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            process_command(command)