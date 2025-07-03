import tkinter as tk
from tkinter import scrolledtext
import threading
from assistant import main as assistant_main
import sys

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gibli - AI Assistant")
        self.root.geometry("500x600")
        self.root.minsize(360, 500)
        self.root.configure(bg="#f4f6f7")

        self.assistant_thread = None
        self.assistant_running = False

        self.setup_ui()
        self.update_buttons()

    def setup_ui(self):
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        title = tk.Label(self.root, text="🤖 Gibli - AI Voice Assistant",
                         font=("Segoe UI", 16, "bold"), fg="#2c3e50", bg="#f4f6f7")
        title.grid(row=0, column=0, pady=(15, 5), padx=10, sticky="n")

        subtitle = tk.Label(self.root, text="Try saying one of these commands:",
                            font=("Segoe UI", 11), fg="#566573", bg="#f4f6f7")
        subtitle.grid(row=1, column=0, pady=(0, 5), padx=10, sticky="n")

        suggestions = [
            "🌐 Search something on Wikipedia",
            "🎵 Play [song name] on YouTube",
            "📺 Open YouTube, Facebook, or Google",
            "😂 Tell me a joke",
            "🌦️ What's the weather in Mumbai?",
            "🔋 What's the battery percentage?",
            "📸 Take a screenshot",
            "📝 Write a note",
            "📖 Read the notes",
            "🎤 Sing a song",
            "💪 Motivate me",
            "🔐 Lock the screen",
            "💬 Send WhatsApp message",
            "⏰ What's the time?",
            "👋 Who are you?",
            "❌ Exit or shutdown"
        ]

        self.suggestion_box = tk.Listbox(self.root, font=("Segoe UI", 10), height=10,
                                         bg="#ffffff", fg="#2c3e50", highlightthickness=0,
                                         borderwidth=1, selectbackground="#d6eaf8",
                                         activestyle="none")
        for item in suggestions:
            self.suggestion_box.insert(tk.END, item)
        self.suggestion_box.grid(row=2, column=0, padx=15, pady=10, sticky="nsew")

        log_label = tk.Label(self.root, text="📜 Assistant Logs",
                             font=("Segoe UI", 11, "bold"), fg="#2c3e50", bg="#f4f6f7")
        log_label.grid(row=3, column=0, pady=(5, 5), padx=10, sticky="w")

        self.console = scrolledtext.ScrolledText(self.root, height=8, state='disabled',
                                                 font=("Consolas", 10), bg="#ffffff",
                                                 fg="#2c3e50", borderwidth=1, relief="solid")
        self.console.grid(row=4, column=0, padx=15, pady=5, sticky="nsew")

        # Buttons frame
        self.button_frame = tk.Frame(self.root, bg="#f4f6f7")
        self.button_frame.grid(row=5, column=0, pady=10)

        self.start_button = tk.Button(self.button_frame, text="▶️ Start Assistant",
                                      command=self.start_assistant, font=("Segoe UI", 11, "bold"),
                                      bg="#27ae60", fg="white", activebackground="#229954",
                                      activeforeground="white", relief="flat", padx=15, pady=8,
                                      cursor="hand2")

        self.stop_button = tk.Button(self.button_frame, text="⏹️ Stop Assistant",
                                     command=self.stop_assistant, font=("Segoe UI", 11, "bold"),
                                     bg="#c0392b", fg="white", activebackground="#922b21",
                                     activeforeground="white", relief="flat", padx=15, pady=8,
                                     cursor="hand2")

    def start_assistant(self):
        if self.assistant_thread and self.assistant_thread.is_alive():
            return
        self.assistant_thread = threading.Thread(target=self.run_assistant, daemon=True)
        self.assistant_thread.start()
        self.assistant_running = True
        self.update_buttons()

    def stop_assistant(self):
        self.log("❌ Stopping assistant...")
        sys.exit()

    def run_assistant(self):
        self.log("🟢 Assistant started. Listening for your command...")
        assistant_main(self.log)

    def update_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.pack_forget()

        if self.assistant_running:
            self.stop_button.pack()
        else:
            self.start_button.pack()

    def log(self, message):
        self.console.config(state='normal')
        self.console.insert(tk.END, f"{message}\n")
        self.console.config(state='disabled')
        self.console.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()
