

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def main():
    speak("Hello! I am jarvis . How can I help you today?")

    while True:
        command = listen()

        if command:
            if "hello" in command:
                speak("Hello! How can I assist you?")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")
            elif "search" in command:
                query = command.split("search")[1].strip()
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {query}")
            elif "exit" in command:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("Sorry, I don't understand that command. Can you please repeat?")
        else:
            speak("Sorry, I couldn't hear you. Can you please repeat your command?")

if __name__ == "__main__":
    main()
