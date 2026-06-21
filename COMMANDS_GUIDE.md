# Voice-Controlled Assistant - Supported Commands Documentation

## Overview
This document lists all supported voice commands for the Voice-Controlled Assistant.

---

## GREETING COMMANDS

### Command: "hello", "hi", "hey"
**Function:** Greets the user with time-appropriate greeting
**Example Usage:** "Hello" / "Hi" / "Hey"
**Assistant Response:** Returns Good Morning/Afternoon/Evening based on current time

---

## TIME & DATE COMMANDS

### Command: "time"
**Function:** Announces current time
**Example Usage:** "What time is it?" / "Tell me the time" / "Time"
**Assistant Response:** Speaks the current time in 12-hour format (e.g., "The current time is 02:30 PM")

### Command: "date"
**Function:** Announces current date
**Example Usage:** "What's the date?" / "Tell me the date" / "Date"
**Assistant Response:** Speaks the current date (e.g., "Today is Sunday, June 21, 2026")

---

## WEATHER COMMANDS

### Command: "weather"
**Function:** Opens weather information website
**Example Usage:** "Check the weather" / "Weather" / "What's the weather like?"
**Assistant Response:** Opens weather.com in default browser and confirms action

---

## SEARCH & BROWSER COMMANDS

### Command: "search [query]" or "google [query]"
**Function:** Performs Google search for specified query
**Example Usage:** 
  - "Search for Python tutorials"
  - "Google weather in Paris"
  - "Search machine learning"
**Assistant Response:** Opens Google search results in default browser

---

## APPLICATION LAUNCHER COMMANDS

### Command: "open [application]"
**Function:** Opens specified application
**Example Usage:** "Open notepad" / "Open calculator" / "Open Chrome"

**Supported Applications:**
- notepad / Notepad (Text Editor)
- calculator / Calculator (System Calculator)
- chrome (Google Chrome Browser)
- firefox (Firefox Browser)
- youtube (Opens YouTube.com)
- gmail (Opens Gmail.com)
- github (Opens GitHub.com)

**Example Responses:**
- "Opening notepad"
- "Opening chrome"
- "Opening calculator"

---

## ENTERTAINMENT COMMANDS

### Command: "joke" or "funny"
**Function:** Tells a random joke
**Example Usage:** "Tell me a joke" / "Say something funny" / "Joke"
**Assistant Response:** Speaks a random joke from the built-in joke database

**Sample Jokes:**
1. "Why don't scientists trust atoms? Because they make up everything!"
2. "What do you call a fake noodle? An impasta!"
3. "Why did the scarecrow win an award? He was outstanding in his field!"
4. "What do you call a bear with no teeth? A gummy bear!"
5. "Why don't eggs tell jokes? They'd crack each other up!"
6. "What did the ocean say to the beach? Nothing, it just waved!"
7. "How do you organize a space party? You planet!"
8. "What did one wall say to the other wall? I'll meet you at the corner!"

---

## NEWS COMMANDS

### Command: "news"
**Function:** Opens latest news website
**Example Usage:** "Show me the news" / "News" / "What's happening?"
**Assistant Response:** Opens BBC News (bbc.com/news) in default browser

---

## NOTES COMMANDS

### Command: "add note [content]"
**Function:** Saves a note with timestamp
**Example Usage:** 
  - "Add note pick up groceries"
  - "Note meeting at 3 PM"
  - "Add note call mom"
**Assistant Response:** Confirms note was saved with timestamp

**Storage:** Notes are saved in JSON format in `voice_assistant_notes.json` with:
- Note ID
- Content
- Timestamp (YYYY-MM-DD HH:MM:SS)

### Command: "read notes" or "show notes"
**Function:** Reads all saved notes aloud
**Example Usage:** "Read my notes" / "Show notes" / "What notes do I have?"
**Assistant Response:** Lists all saved notes with their IDs and content

---

## HELP COMMAND

### Command: "help" or "commands"
**Function:** Displays all available commands
**Example Usage:** "Help" / "What can you do?" / "Show commands"
**Assistant Response:** Displays help menu with all command options

---

## EXIT COMMANDS

### Command: "exit", "quit", "bye", "goodbye"
**Function:** Terminates the voice assistant
**Example Usage:** "Exit" / "Quit" / "Goodbye" / "Bye"
**Assistant Response:** Says goodbye and closes the application
**Note:** Automatically saves all notes before exiting

---

## SYSTEM INFORMATION

### Microphone Usage
- Uses system microphone for voice input
- Automatically adjusts for ambient noise
- 10-second listening timeout
- Supports multiple microphones

### Speech Recognition
- Uses Google Speech Recognition API (cloud-based)
- Requires internet connection for recognition
- Supports English language input
- Real-time processing and feedback

### Text-to-Speech
- Uses pyttsx3 library
- Adjustable speech rate (default: 150 WPM)
- Adjustable volume (default: 0.9)
- Cross-platform support (Windows, macOS, Linux)

---

## ERROR HANDLING

### Common Errors and Solutions

1. **"Sorry, I didn't understand that"**
   - Speak more clearly
   - Reduce background noise
   - Increase microphone volume

2. **"Error accessing the speech service"**
   - Check internet connection
   - Verify Google API is accessible
   - Restart the assistant

3. **"I didn't hear anything"**
   - Speak louder and clearer
   - Position microphone closer
   - Reduce ambient noise

4. **Application won't open**
   - Verify application name is correct
   - Check if application is installed
   - Try using alternative names

---

## KEYBOARD SHORTCUTS

- **Ctrl+C:** Force exit the assistant (saves notes automatically)
- **Alt+Tab:** Switch between windows while assistant is running

---

## FILE LOCATIONS

- **Main Script:** voice_assistant.py
- **Requirements File:** requirements.txt
- **Notes Storage:** voice_assistant_notes.json (created automatically)
- **Command History:** Stored in memory during session

---

## PERFORMANCE SPECIFICATIONS

- **Response Time:** 2-5 seconds (including cloud processing)
- **Recognition Accuracy:** ~95% (Google Speech Recognition)
- **Language:** English (US)
- **Supported Platforms:** Windows, macOS, Linux
- **Minimum RAM:** 256 MB
- **Internet Required:** Yes (for speech recognition)

---

## TIPS FOR BEST RESULTS

1. **Use Natural Speech:** Speak naturally, not robotically
2. **Complete Sentences:** Use full commands for better recognition
3. **Reduce Noise:** Use in quiet environment
4. **Microphone Position:** Place microphone 6-8 inches from mouth
5. **Clear Pronunciation:** Pronounce words clearly
6. **Avoid Interruptions:** Let the assistant finish listening before speaking

---

## FUTURE ENHANCEMENTS

Potential commands for future versions:
- Weather with location specification
- Email sending via voice
- Reminder and alarm setting
- Music playback control
- IoT device control
- Calendar integration
- Document creation
- Code execution
- Multi-language support

---

## TROUBLESHOOTING GUIDE

**Issue:** Microphone not detected
**Solution:** Check system audio settings, test microphone on other apps

**Issue:** Slow recognition
**Solution:** Check internet connection, move closer to router

**Issue:** Notes not saving
**Solution:** Check file permissions, ensure disk space available

**Issue:** Voice output not working
**Solution:** Check speaker volume, verify TTS engine installation

---

**Document Version:** 1.0
**Last Updated:** June 2026
**Assistant Version:** 1.0

For support and updates, visit: https://github.com/
