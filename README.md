# Intelligent Multilingual Speech-to-Action System

An AI-powered system that listens to voice commands and performs actions on your computer, such as searching the web, opening applications, and telling the time.

## 🚀 Features
- **Voice Recognition**: Uses Google Speech Recognition for high accuracy.
- **Natural Language Parsing**: Intelligent pattern matching to understand commands.
- **Multilingual Ready**: Can be configured for multiple languages (English, Spanish, etc.).
- **Text-to-Speech**: Provides audio feedback for a complete interactive experience.
- **Automated Actions**:
    - "Search for [topic]" -> Opens your browser and searches Google.
    - "Open [app/website]" -> Opens the specified application or URL.
    - "What time is it?" -> Tells the current time.

## 🛠️ Setup

1. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Microphone Access**:
   Make sure your microphone is connected and set as the default recording device.

3. **Run the System**:
   ```bash
   python main.py
   ```

## 🌍 Multilingual Support
To change the language, modify the `language` parameter in `main.py`:
- English: `en-US` or `en-IN`
- Spanish: `es-ES`
- French: `fr-FR`
- Mandarin: `zh-CN`

## 🏗️ Expanding Actions
You can add new actions in `actions.py` and map them in `processor.py`.

### Example:
- **Command**: "Hey assistant, search for quantum computing"
- **Action**: Opens Chrome with the search results for "quantum computing".
