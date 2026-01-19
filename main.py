import speech_recognition as sr
import pyttsx3
import processor
import colorama
import config
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Default voice
engine.setProperty('rate', config.SPEECH_RATE)            # Speed of speech

def speak(text):
    print(f"{Fore.CYAN}Assistant: {text}{Style.RESET_ALL}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\n{Fore.GREEN}Listening...{Style.RESET_ALL}")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print(f"{Fore.YELLOW}Recognizing...{Style.RESET_ALL}")
        query = recognizer.recognize_google(audio, language=config.DEFAULT_LANGUAGE)
        print(f"{Fore.WHITE}User said: {query}\n{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Could not recognize speech. Please try again.{Style.RESET_ALL}")
        return None
    return query

def main():
    speak(f"Hello {config.USER_NAME}! I am your Intelligent Speech-to-Action System. How can I help you today?")
    
    while True:
        query = listen()
        
        if query:
            if "exit" in query.lower() or "stop" in query.lower() or "quit" in query.lower():
                speak("Goodbye! Have a great day.")
                break
                
            response = processor.process_command(query, original_lang=config.DEFAULT_LANGUAGE)
            speak(response)

if __name__ == "__main__":
    main()
