"""
Voice-Controlled Assistant
A Python-based intelligent voice assistant that performs system tasks via voice commands.

Features:
- Voice recognition and text-to-speech conversion
- System task automation (open apps, get time/date, etc.)
- Extensible command system
- Interactive joke, news, and notes modules
- Continuous listening loop with exit commands
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
import sys
import os
import json
from pathlib import Path

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure TTS engine
engine.setProperty('rate', 150)  # Words per minute
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Try to set a better voice if available
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)

# Notes storage file
NOTES_FILE = "voice_assistant_notes.json"


class VoiceAssistant:
    """Main voice assistant class"""
    
    def __init__(self):
        self.is_running = True
        self.notes = self.load_notes()
        self.command_history = []
        
    def speak(self, text):
        """Speak out the given text"""
        print(f"🤖 Assistant: {text}")
        engine.say(text)
        engine.runAndWait()
    
    def listen(self):
        """Listen to microphone input and convert to text"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=10)
            
            # Try Google Speech Recognition
            print("🔄 Processing...")
            text = recognizer.recognize_google(audio)
            print(f"👤 You said: {text}")
            return text.lower()
            
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that. Please repeat.")
            return None
        except sr.RequestError as e:
            self.speak(f"Error accessing the speech service. {str(e)}")
            return None
        except sr.Timeout:
            self.speak("I didn't hear anything. Please try again.")
            return None
    
    def get_greeting(self):
        """Get appropriate greeting based on time of day"""
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning!"
        elif hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"
    
    def get_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def get_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
    
    def get_weather_info(self):
        """Open weather information (using web search)"""
        self.speak("Opening weather information")
        webbrowser.open("https://weather.com")
    
    def open_browser(self, query):
        """Open browser and search for query"""
        self.speak(f"Searching for {query} on Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    def open_application(self, app_name):
        """Open an application"""
        apps = {
            'notepad': 'notepad.exe' if sys.platform == 'win32' else 'gedit',
            'calculator': 'calc.exe' if sys.platform == 'win32' else 'gnome-calculator',
            'chrome': 'chrome' if sys.platform != 'win32' else 'chrome.exe',
            'firefox': 'firefox.exe' if sys.platform == 'win32' else 'firefox',
            'youtube': 'https://www.youtube.com',
            'gmail': 'https://www.gmail.com',
            'github': 'https://www.github.com',
        }
        
        app_name = app_name.strip().lower()
        
        if app_name in apps:
            app_path = apps[app_name]
            if app_path.startswith('http'):
                self.speak(f"Opening {app_name}")
                webbrowser.open(app_path)
            else:
                try:
                    self.speak(f"Opening {app_name}")
                    if sys.platform == 'win32':
                        subprocess.Popen(app_path)
                    else:
                        subprocess.Popen(['open', app_path] if sys.platform == 'darwin' else [app_path])
                except Exception as e:
                    self.speak(f"Could not open {app_name}. {str(e)}")
        else:
            self.speak(f"I don't have {app_name} in my list. Try a different application.")
    
    def tell_joke(self):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "How do you organize a space party? You planet!",
            "What did one wall say to the other wall? I'll meet you at the corner!",
        ]
        import random
        joke = random.choice(jokes)
        self.speak(joke)
    
    def get_news(self):
        """Open news website"""
        self.speak("Opening BBC News for you")
        webbrowser.open("https://www.bbc.com/news")
    
    def add_note(self, note_content):
        """Add a note"""
        if note_content:
            note_id = len(self.notes) + 1
            self.notes[str(note_id)] = {
                'content': note_content,
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.save_notes()
            self.speak(f"Note added: {note_content}")
        else:
            self.speak("Please provide the note content")
    
    def read_notes(self):
        """Read all saved notes"""
        if not self.notes:
            self.speak("You don't have any notes yet")
            return
        
        self.speak(f"You have {len(self.notes)} notes")
        for note_id, note in self.notes.items():
            self.speak(f"Note {note_id}: {note['content']}")
    
    def load_notes(self):
        """Load notes from file"""
        if Path(NOTES_FILE).exists():
            try:
                with open(NOTES_FILE, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_notes(self):
        """Save notes to file"""
        try:
            with open(NOTES_FILE, 'w') as f:
                json.dump(self.notes, f, indent=4)
        except Exception as e:
            print(f"Error saving notes: {str(e)}")
    
    def process_command(self, command):
        """Process voice command and execute appropriate action"""
        if not command:
            return
        
        self.command_history.append(command)
        
        # Greeting
        if 'hello' in command or 'hi' in command or 'hey' in command:
            self.speak(self.get_greeting())
        
        # Time and Date
        elif 'time' in command:
            self.get_time()
        elif 'date' in command:
            self.get_date()
        
        # Weather
        elif 'weather' in command:
            self.get_weather_info()
        
        # Search
        elif 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').replace('for', '').strip()
            if query:
                self.open_browser(query)
            else:
                self.speak("What would you like me to search for?")
        
        # Open application
        elif 'open' in command:
            app = command.replace('open', '').strip()
            self.open_application(app)
        
        # Jokes
        elif 'joke' in command or 'funny' in command:
            self.tell_joke()
        
        # News
        elif 'news' in command:
            self.get_news()
        
        # Notes
        elif 'add note' in command or 'note' in command and 'add' in command:
            note_content = command.replace('add note', '').replace('note', '').strip()
            self.add_note(note_content)
        elif 'read notes' in command or 'show notes' in command:
            self.read_notes()
        
        # Help
        elif 'help' in command or 'commands' in command:
            self.show_help()
        
        # Exit
        elif 'exit' in command or 'quit' in command or 'bye' in command or 'goodbye' in command:
            self.speak("Goodbye! Thank you for using the voice assistant.")
            self.is_running = False
        
        # Default response
        else:
            self.speak("I'm not sure how to help with that. Say 'help' to see available commands.")
    
    def show_help(self):
        """Display help information"""
        help_text = """
        Available commands:
        - Hello, Hi, Hey: Get greeting
        - Time: Get current time
        - Date: Get current date
        - Weather: Check weather
        - Search [query]: Search on Google
        - Open [app]: Open an application
        - Tell joke: Hear a random joke
        - News: Get latest news
        - Add note [content]: Save a note
        - Read notes: Read all saved notes
        - Help: Show this help menu
        - Exit, Quit, Bye, Goodbye: Exit assistant
        """
        print(help_text)
        self.speak("Here are the available commands. Check the console for the full list.")
    
    def run(self):
        """Main listening loop"""
        self.speak(self.get_greeting())
        self.speak("I'm your voice assistant. Say 'help' to see what I can do.")
        
        while self.is_running:
            command = self.listen()
            if command:
                self.process_command(command)
        
        # Save notes before exiting
        self.save_notes()


def main():
    """Main entry point"""
    print("=" * 60)
    print("  VOICE-CONTROLLED ASSISTANT")
    print("  Created for AI-Powered Automation")
    print("=" * 60)
    print("\n🎤 Make sure your microphone is connected and working!")
    print("📢 Speak clearly and at a moderate pace")
    print("🔴 Say 'exit' or 'quit' to stop the assistant\n")
    
    assistant = VoiceAssistant()
    
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\n\nAssistant terminated by user.")
        assistant.save_notes()
    except Exception as e:
        print(f"Error: {str(e)}")
        assistant.save_notes()


if __name__ == "__main__":
    main()
