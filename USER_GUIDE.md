# 🎙️ User Guide: Intelligent Speech-to-Action System

Welcome to your AI-powered voice assistant! This system allows you to control your computer, browse the web, and perform tasks just by speaking.

---

## 🚀 How to Start
1.  **Run the System**: Open your terminal and run `python main.py`.
2.  **Wait for Greeting**: You will hear "Hello Baibhav Rajkumar! How can I help you today?".
3.  **Speak Naturally**: Once you see `Listening...`, give any of the commands below.

---

## 📺 YouTube Superpowers
| Command | Action |
| :--- | :--- |
| *"Open YouTube"* | Opens the YouTube homepage. |
| *"Search YouTube for [Topic]"* | Directly searches YouTube for your specific topic. |
| *"Play/Open the [Number] video"* | Navigates to the specific video in the results (e.g., "1st", "5th", "10th"). |
| *"Pause"* / *"Play"* | Toggles the video playback once you are on the page. |

---

## 🌐 Web & Browser Control
| Command | Action |
| :--- | :--- |
| *"Search for [Topic]"* | Performs a Google search. |
| *"Open [Website URL]"* | Opens a specific site (e.g., "open google.com"). |
| *"Go Back"* | Goes to the previous page in your browser. |
| *"Go Forward"* | Goes to the next page in your browser. |
| *"Close Tab"* | Specifically closes the active browser tab. |

---

## 🧮 Math & Desktop
| Command | Action |
| :--- | :--- |
| *"Calculate [Equation]"* | Solves math (e.g., "Calculate 50 plus 20" or "What is 10 times 5"). |
| *"Open Calculator"* | Launches the Windows Calculator app. |
| *"Open Notepad"* | Launches a fresh Notepad window. |
| *"Close It"* / *"Close This"* | Closes the entire active desktop application (Alt+F4). |

---

## 🌍 Multilingual Support
You can speak in multiple languages! The assistant will translate your intent into English commands automatically. Supported languages include:
- English, Spanish, Hindi, Mandarin, French, and more.
- *Change `DEFAULT_LANGUAGE` in `config.py` to switch.*

---

## ⚙️ Customization
To personalize the system, edit `config.py`:
- **USER_NAME**: Change who the assistant greets.
- **APP_MAPPING**: Add keywords for your favorite apps (e.g., `"game": "minecraft.exe"`).

---

## 🛑 How to Stop
Simply say **"Exit"**, **"Stop"**, or **"Quit"** at any time to shut down the assistant.
