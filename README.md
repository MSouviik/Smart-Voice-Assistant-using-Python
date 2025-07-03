# 🤖 Gibli – Your Smart Voice Assistant (2025 Edition)

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
