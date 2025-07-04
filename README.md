# 🤖 Gibli – Your Smart Voice Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Cross--Platform-blueviolet)
![Status](https://img.shields.io/badge/Build-Stable-success)

Welcome to **Gibli**, the all-knowing, always-ready voice assistant built in Python with a sleek GUI! 🎙️✨

Gibli is here to help you with everything from telling jokes to checking the weather, sending WhatsApp messages, locking your screen, and even dishing out motivational quotes—because let’s be honest, life’s better with a helpful robot sidekick.

---

## 🤯 Why Gibli?

> One night, at 3 AM, I asked my PC to "do something useful"... and it just stared back at me 🧍‍♂️💻.  
> That’s when I realized — my PC needed **purpose**... and **voice**.  
> Hence, **Gibli** was born – the sarcastic, wise, AI-powered roommate I never knew I needed.

---

## 🧩 Features

- 🎤 **Voice Recognition**
- 🧠 **AI-Powered Answers**
- 🧹 **Profanity Detection with Smart Replies**
- 💬 **Dynamic Greetings and Birthday Wishes**
- 🌤️ **Weather Info (Just Say the City)**
- 🔋 **Battery Status Reporting**
- 🎧 **MP3 Music Playback**
- 📸 **Take Screenshots**
- 🗒️ **Take & Read Notes**
- 💌 **Send WhatsApp Messages**
- 🧽 **Sassy, Humorous, or Motivational Replies**
- 💂‍♀️ **Less Robotic Female Voice**
- 🖥️ **Modern Tkinter GUI Interface**
- 🛠️ **Easy to Extend & Customize**

---

## 🚀 Quick Launch (EXE Mode)

> ✅ Just want to run it without coding?

1. Go to the `dist/` folder.
2. Double-click on `assistant_gui.exe`.

🎉 That’s it! Your assistant is ready to help.

---

## 🛠️ Developer Setup (Clone & Customize)

Want to add your own features or help improve Gibli? Follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/gibli-voice-assistant.git
cd gibli-voice-assistant

# 2. Install required dependencies
pip install -r requirements.txt

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 5. Package your application with PyInstaller

pyinstaller --noconsole --onefile assistant_gui.py ^
 --add-data "assets;assets" ^
 --add-data "venv\Lib\site-packages\better_profanity\alphabetic_unicode.json;better_profanity"

# 🛠 Alternate Packaging Command (if above fails)

pyinstaller --noconsole --onefile assistant_gui.py ^
 --add-data="assets:assets" ^
 --add-data="C:\\Users\\YourName\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\better_profanity:better_profanity"
```

---

## 🌟 Ideas for Future

- 💬 **ChatGPT-style long-form conversations**  
- 🌐 **Real-time translation**  
- 🧠 **Memory-based conversations**  
- 🎶 **Sing songs with lyrics**  
- 🔌 **Plugin support**

---

## 🙌 Acknowledgements

Made using **Python 3.12** ❤

Big thanks to the open-source community and the libraries that power **Gibli**:

- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)
- [`tkinter`](https://docs.python.org/3/library/tkinter.html)
- [`better_profanity`](https://pypi.org/project/better-profanity/)
- [`requests`](https://pypi.org/project/requests/)
- *...and many more!*

---

## 🪪 License

**MIT License** – use it, modify it, share it… just don’t turn it evil 👿

---

## 💬 Quote

> “If Iron Man can have Jarvis, why can’t we have Gibli?” – You, after using this assistant.

---

## 🔗 Connect

📫 **Want to contribute or give feedback?**  
Fork this project, ⭐ star it, and send a pull request!

---

## 👨‍💻 Developer

Built with ☕ and ❤️ by [@MSouviik](https://github.com/MSouviik)  

Pull requests are welcome!  
**Fork it, build it, break it, fix it.**
