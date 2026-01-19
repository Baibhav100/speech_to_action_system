import actions
import re
from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def process_command(text, original_lang='en'):
    # Translate to English for processing (canonical command language)
    if original_lang.split('-')[0] != 'en':
        processed_text = translate_to_english(text)
        print(f"Translated Command: {processed_text}")
    else:
        processed_text = text
        
    processed_text = processed_text.lower()
    
    # 1. Video selection (Open/Play sequence) - MUST COME BEFORE generic 'play'
    # Match "play the 5th video", "open second video", etc.
    num_map = {
        "first": "1", "second": "2", "third": "3", "fourth": "4", "fifth": "5",
        "sixth": "6", "seventh": "7", "eighth": "8", "ninth": "9", "tenth": "10",
        "1st": "1", "2nd": "2", "3rd": "3", "4th": "4", "5th": "5", "10th": "10"
    }
    
    # Very flexible regex for video selection
    video_pattern = r"(?:play|open|click) (?:the )?(\d+|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)(?:st|nd|rd|th)? video"
    video_match = re.search(video_pattern, processed_text)
    
    if video_match:
        num_str = video_match.group(1).lower()
        num = num_map.get(num_str, num_str)
        # If it's a digit now, call select_video
        if num.isdigit():
            return actions.select_video(num)

    # 2. YouTube Search/Open Logic
    if "youtube" in processed_text:
        if "search" in processed_text:
            query = processed_text.split("search")[-1].replace("youtube", "").strip()
            return actions.search_youtube(query)
        elif "open" in processed_text:
            return actions.open_youtube()

    # 3. Media control logic - Only trigger if it's NOT a sequence command
    # Use word boundaries to avoid catching 'play' inside other words
    if re.search(r"\b(pause|resume)\b", processed_text) or (re.search(r"\bplay\b", processed_text) and "video" not in processed_text):
        return actions.toggle_play_pause()
    
    # Or if they just say "play video" or "pause video" without a number
    if processed_text.strip() in ["play video", "pause video", "play", "pause"]:
        return actions.toggle_play_pause()

    # 4. Calculator/Math Logic
    if "calculate" in processed_text or "what is" in processed_text or any(op in processed_text for op in ["plus", "minus", "multiply", "divide"]):
        expression_to_calc = processed_text.replace("calculate", "").replace("what is", "").strip()
        if expression_to_calc:
            return actions.calculate(expression_to_calc)

    # 5. Closing logic
    if "close it" in processed_text or "close this" in processed_text:
        return actions.close_app()
    if "close tab" in processed_text:
        return actions.close_tab()

    # 6. Navigation logic
    if "go back" in processed_text:
        return actions.go_back()
    if "go forward" in processed_text:
        return actions.go_forward()

    # Search logic (Generic)
    search_match = re.search(r"search (?:for )?(.+)", processed_text)
    if search_match:
        query = search_match.group(1).strip()
        return actions.search_google(query)
    
    # Open logic (Generic)
    if "open" in processed_text:
        # Check for browser specifically
        if "browser" in processed_text or "chrome" in processed_text or "google" in processed_text:
            if "search" not in processed_text:
                return actions.open_website("google.com")
        
        target = processed_text.split("open")[-1].strip()
        if "." in target or "www" in target:
            return actions.open_website(target)
        else:
            return actions.open_app(target)
            
    # Time logic
    if "time" in processed_text:
        return actions.get_time()
        
    if "hello" in processed_text or "hi " in processed_text:
        return f"Hello {config.USER_NAME}! How can I assist you with your tasks today?"
        
    return "I heard you say: '" + text + "'. I'm not programmed for that specific action yet."
