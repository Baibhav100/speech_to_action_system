import webbrowser
import os
import subprocess
import config
import pyautogui
import time

def search_google(query):
    print(f"Searching for: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for {query}"

def open_youtube():
    print("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"

def search_youtube(query):
    print(f"Searching YouTube for: {query}")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    return f"Searching YouTube for {query}"

def open_website(url):
    print(f"Opening: {url}")
    if not url.startswith('http'):
        url = 'https://' + url
    webbrowser.open(url)
    return f"Opening {url}"

def open_app(app_name):
    app_to_open = config.APP_MAPPING.get(app_name.lower(), app_name)
    print(f"Opening app: {app_to_open}")
    try:
        os.system(f"start {app_to_open}")
        return f"Opening {app_name}"
    except Exception as e:
        return f"Failed to open {app_name}: {str(e)}"

# Navigation and Controls
def go_back():
    pyautogui.hotkey('alt', 'left')
    return "Going back"

def go_forward():
    pyautogui.hotkey('alt', 'right')
    return "Going forward"

def close_app():
    pyautogui.hotkey('alt', 'f4')
    return "Closing application"

def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    return "Closing tab"

def toggle_play_pause():
    pyautogui.press('space') # Standard for most web players
    return "Toggling play pause"

def select_video(number):
    try:
        n = int(number)
        print(f"Navigating to video {n}...")
        
        # 1. Focus the browser and escape any overlays
        pyautogui.click(pyautogui.size()[0]//2, pyautogui.size()[1]//2) # Click center to focus
        pyautogui.press('esc')
        time.sleep(0.5)
        
        # 2. YouTube usually needs a few initial tabs to get into the grid/list area
        # from the search bar/header.
        initial_tabs = 8
        for _ in range(initial_tabs):
            pyautogui.press('tab')
            
        # 3. Each video item on YouTube usually has about 4-6 tabbable elements
        # (thumbnail, title, avatar, etc.). 
        # We need to skip n-1 videos to get to the nth one.
        tabs_per_video = 5
        total_skip_tabs = (n - 1) * tabs_per_video
        
        for i in range(total_skip_tabs):
            pyautogui.press('tab')
            if i % 10 == 0: # Small breather for long sequences (like 10th+ video)
                time.sleep(0.1)
                
        # 4. Press Enter to play
        pyautogui.press('enter')
        return f"Playing the {number} video for you, Baibhav."
    except Exception as e:
        return f"Sorry Baibhav, I had trouble navigating to that video: {str(e)}"

def calculate(expression):
    # Map spoken words to symbols
    expr = expression.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("times", "*").replace("divided by", "/").replace("add", "+").replace("substract", "-").replace("multiply", "*").replace("divide", "/")
    
    # Simple security check (only allow digits and operators)
    import re
    if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expr):
        return "I can only process simple mathematical expressions."
        
    try:
        # We'll use the calculator app via keyboard for visual feedback, 
        # but calculate the result internally to speak it back
        result = eval(expr)
        
        # Type the expression into calculator for the user to see
        for char in expr:
            pyautogui.press(char)
        pyautogui.press('enter')
        
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"I couldn't calculate that: {str(e)}"

def get_time():
    import datetime
    now = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {now}"
