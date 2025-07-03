import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pywhatkit
import shutil
import random
import pyjokes
import psutil
import ctypes
import requests
from playsound import playsound
import getpass
import subprocess
import sys
import pyautogui
from better_profanity import profanity
import asyncio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
assistant_name = "Gibli"
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8

# Updated speak with logging support
def speak(text, log_fn=None):
    if log_fn:
        log_fn(f"{assistant_name}: {text}")
    else:
        print(f"{assistant_name}: {text}")
        
    engine.say(text)
    engine.runAndWait()

def install_female_voice_windows(log_fn=None):
    speak("Checking available voices.", log_fn)
    voices = engine.getProperty('voices')
    female_found = any("female" in v.name.lower() or "zira" in v.name.lower() for v in voices)

    if not female_found:
        speak("Female voice not found. Attempting to download Microsoft Zira voice.", log_fn)
        try:
            subprocess.run([
                "powershell",
                "-Command",
                "Add-WindowsCapability -Online -Name 'Language.Basic~~~en-US~0.0.1.0'"
            ], check=True)
            speak("Microsoft Zira voice installed. Please restart the assistant.", log_fn)
            sys.exit()
        except subprocess.CalledProcessError:
            speak("Failed to install the voice. Please install it manually from settings.", log_fn)
            sys.exit()

install_female_voice_windows()

female_voice = next((v for v in voices if "female" in v.name.lower() or "zira" in v.name.lower()), voices[0])
engine.setProperty('voice', female_voice.id)
engine.setProperty('rate', 200)

try:
    user_name = getpass.getuser()
    if not user_name:
        user_name = os.getlogin()
except Exception:
    user_name = os.environ.get('USERNAME', 'User')

def wish_me(log_fn=None):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(f"Good Morning, {user_name}!", log_fn)
    elif 12 <= hour < 18:
        speak(f"Good Afternoon, {user_name}!", log_fn)
    else:
        speak(f"Good Evening, {user_name}!", log_fn)

    greetings = [
        "Hello there! Ready to start the day?",
        "Hey! I'm all ears.",
        "Hi! Let's conquer some tasks today.",
        "Welcome back! Gibli at your service.",
        "Good to see you. How can I help today?"
    ]
    speak(random.choice(greetings), log_fn)

def take_command(log_fn=None):
    with sr.Microphone() as source:
        speak("Listening now...", log_fn)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.", log_fn)
            return ""

    try:
        speak("Recognizing...", log_fn)
        return recognizer.recognize_google(audio, language='en-in').lower()
    except sr.UnknownValueError:
        speak("I couldn't understand. Could you please repeat?", log_fn)
        return ""
    except sr.RequestError:
        speak("Recognition service is unreachable.", log_fn)
        return ""


def tell_joke(log_fn=None):
    joke = pyjokes.get_joke()
    speak("Here's a joke for you.", log_fn)
    speak(joke, log_fn)

def get_battery_status(log_fn=None):
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent.", log_fn)
    else:
        speak("Sorry, I couldn't access battery information.", log_fn)

def lock_screen(log_fn=None):
    speak("Locking the screen now.", log_fn)
    ctypes.windll.user32.LockWorkStation()

def get_weather(log_fn=None):
    speak("For which city do you want the weather update?", log_fn)
    city = take_command(log_fn)
    if not city:
        speak("I didn't get the city name.", log_fn)
        return

    try:
        speak(f"Getting weather for {city}", log_fn)
        geo_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
        geo_data = geo_response.json()

        if "results" in geo_data and len(geo_data["results"]) > 0:
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]

            weather_response = requests.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather = weather_response.json()["current_weather"]
            speak(f"The temperature in {city} is {weather['temperature']}°C with wind speed of {weather['windspeed']} km/h.", log_fn)
        else:
            speak("Sorry, I couldn't find the city.", log_fn)
    except Exception:
        speak("Unable to fetch weather information.", log_fn)

def open_app(app_name, log_fn=None):
    app_paths = {
        "vscode": shutil.which("code"),
        "notepad": shutil.which("notepad"),
        "calculator": shutil.which("calc"),
    }
    path = app_paths.get(app_name.lower())
    if path:
        speak(f"Opening {app_name}.", log_fn)
        os.system(f'"{path}"')
    else:
        speak(f"Sorry, I couldn't find {app_name} installed.", log_fn)

def repeat_after_me(query, log_fn=None):
    phrase = query.lower().replace("repeat after me", "").strip()
    if phrase:
        speak(phrase, log_fn)
    else:
        speak("What should I repeat?", log_fn)
        phrase = take_command(log_fn)
        if phrase:
            speak(phrase, log_fn)

def sing_song(log_fn=None):
    song_path = os.path.join(os.path.dirname(__file__), 'assets', 'assistantsong.mp3')
    if os.path.exists(song_path):
        speak("Here's a song just for you.", log_fn)
        playsound(song_path)
    else:
        speak("Sorry, I couldn't find the song file.", log_fn)


def motivational_quote(log_fn=None):
    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Stay positive, work hard, make it happen."
    ]
    speak(random.choice(quotes), log_fn)

def take_screenshot(log_fn=None):
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, f"screenshot_{int(time.time())}.png")
    pyautogui.screenshot().save(screenshot_path)
    speak(f"Screenshot saved as {screenshot_path}", log_fn)


def write_note(log_fn=None):
    speak("What should I write?", log_fn)
    note = take_command(log_fn)
    notes_dir = "notes"
    os.makedirs(notes_dir, exist_ok=True)
    note_file_path = os.path.join(notes_dir, "note.txt")
    with open(note_file_path, "a") as f:
        f.write(f"{datetime.datetime.now()}: {note}\n")
    speak("Note saved.", log_fn)

def read_notes(log_fn=None):
    if os.path.exists("note.txt"):
        with open("note.txt", "r") as f:
            speak("Here's what you noted down:", log_fn)
            speak(f.read(), log_fn)
    else:
        speak("You don't have any saved notes yet.", log_fn)

def confirm_action(log_fn=None):
    speak("Are you sure? - Yes || Sure", log_fn)
    response = take_command(log_fn)
    return 'yes' in response or 'sure' in response

def calibrate_microphone(log_fn=None):
    with sr.Microphone() as source:
        speak("Calibrating for background noise. Please wait a moment...", log_fn)
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        speak("Calibration done. I'm ready to listen.", log_fn)

def main(log_fn=None):
    
    calibrate_microphone(log_fn)
    wish_me(log_fn)

    while True:
        query = take_command(log_fn)
        if not query:
            continue

        if any(wake_word in query for wake_word in [
            f"hi {assistant_name.lower()}",
            f"hey {assistant_name.lower()}",
            f"hello {assistant_name.lower()}",
            "hi",
            "hello",
            "hey"
        ]):
            speak("Hi there! What can I do for you?", log_fn)
            continue

        if 'repeat after me' in query or 'repeat the sentance' in query:
            repeat_after_me(query, log_fn)

        profanity.load_censor_words()
        if profanity.contains_profanity(query):
            responses = [
                "That's not very nice. Let's keep it friendly.",
                "I’m here to help, not to be insulted.",
                "Please be respectful.",
                "Let's keep things positive."
            ]
            speak(random.choice(responses), log_fn)
            continue

        if 'birthday' in query:
            speak("Happy Birthday! Wishing you a wonderful year ahead!", log_fn)
            continue

        if 'wikipedia' in query or 'search in wikipedia' in query:
            speak('Searching Wikipedia...', log_fn)
            result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
            speak("According to Wikipedia:", log_fn)
            speak(result, log_fn)

        elif 'yourself' in query or 'who are you' in query:
            speak(f"I'm {assistant_name}, your AI assistant, built to help you daily.", log_fn)

        elif 'joke' in query or 'tell a joke' in query:
            tell_joke(log_fn)

        elif 'weather' in query:
            get_weather(log_fn)

        elif 'battery' in query or 'battery percentage' in query:
            get_battery_status(log_fn)

        elif 'lock screen' in query or 'lock the screen' in query:
            if(confirm_action(log_fn)):
                lock_screen(log_fn)
            else:
                speak("Cancelled locking the screen.", log_fn)

        elif 'open' in query:
            if "youtube" in query:
                webbrowser.open("https://youtube.com")
            elif "facebook" in query:
                webbrowser.open("https://facebook.com")
            elif "google" in query:
                webbrowser.open("https://google.com")
            elif "v s code" in query or "vs code" in query:
                open_app("vscode", log_fn)
            elif "calculator" in query:
                open_app("calculator", log_fn)
            elif "notepad" in query:
                open_app("notepad", log_fn)

        elif 'play' in query or 'play song' in query:
            song = query.replace('play', '').strip()
            speak(f"Playing {song}", log_fn)
            pywhatkit.playonyt(song)

        elif 'sing a song' in query or 'sing song' in query:
            sing_song(log_fn)

        elif 'motivate me' in query or 'motivation' in query or 'motivational' in query:
            motivational_quote(log_fn)

        elif 'screenshot' in query or 'take screenshot' in query:
            take_screenshot(log_fn)

        elif 'write note' in query or 'take note' in query or 'take down note' in query or 'write down' in query:
            write_note(log_fn)

        elif 'read notes' in query or 'read the notes' in query or 'read out' in query:
            read_notes(log_fn)

        elif 'send whatsapp message' in query:
            speak("Sending a test WhatsApp message.", log_fn)
            pywhatkit.sendwhatmsg("+919674656298", "Hello from Gibli!", datetime.datetime.now().hour, datetime.datetime.now().minute + 2)

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"It's {current_time}", log_fn)

        elif 'exit' in query or 'shutdown' in query or 'quit' in query:
            speak("Shutting down. Catch you later!", log_fn)
            break

        time.sleep(3)

def start_assistant():
    main()

if __name__ == "__main__":
    start_assistant()
