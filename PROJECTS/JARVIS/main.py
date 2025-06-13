# Import necessary libraries
import speech_recognition as sr  # Used for recognizing speech from microphone
import webbrowser  # (Currently unused) Can be used to open web pages if needed
import pyttsx3  # Used for converting text to speech
import musicLibrary
import requests
import client

# pip install pocketsphinx (optional if you want offline speech recognition)

# Create a Recognizer object (used for speech recognition)
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "pub_5f570cf9f6314a41ac6db56be6e5ea33"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to make Jarvis speak any text
def speak(text):
  engine.say(text)  # Pass the text to the TTS engine
  engine.runAndWait()  # Run the TTS engine and wait until it finishes speaking 

# Define a function to process the recognized command
def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  elif c.lower().startswith("play"):
    song = c.lower().replace("play", "", 1).strip()
    link = musicLibrary.music.get(song)
    if link:
        webbrowser.open(link)
    else:
        speak("Song not found in library.")
  
  elif "news" in c.lower():
    r = requests.get("https://newsdata.io/api/1/news?apikey=pub_5f570cf9f6314a41ac6db56be6e5ea33&category=technology&language=en")

    if r.status_code == 200:
      # Parse the JSON response
      data = r.json()

      # Extract the news headlines
      articles = data.get('results', [])


      # Print the headlines
      for article in articles:
        title = article.get('title', 'No Title Found')
        speak(title)

   
  

# Entry point of the program
if __name__ == "__main__":
  speak("Initializing Jarvis....")  # Speak the initialization message

  while True:  # Infinite loop to keep Jarvis running
    # Listen for the wake word "Jarvis"
    # Obtain audio from the microphone
    
    # Create a new Recognizer object (optional, you can reuse the previous one too)
    r = sr.Recognizer()

    print("recognizing...")  # Just a print statement indicating program is ready to listen
    
    try:
      # Start listening from microphone
      with sr.Microphone() as source:  # Open microphone stream
        print("Listening...")  # Indicate listening started
        # Listen for audio input with some timeout and phrase limit
        audio = r.listen(source, timeout=5, phrase_time_limit=3)  
        # timeout = max time to wait for speech to start
        # phrase_time_limit = max duration of speech capture

      # Use Google's speech recognition service to convert audio to text
      word = r.recognize_google(audio)  
      
      # Check if the recognized word is "jarvis" (wake word)
      if(word.lower() == "jarvis"):
        speak("Ya")  # If wake word detected, reply "Ya"

        # Now listen for the actual command
        with sr.Microphone() as source:
          print("Jarvis Active...")  # Indicate ready for command
          audio = r.listen(source, timeout=10, phrase_time_limit=8) 
          # Same: waiting for speech with timeout and max length
          command = r.recognize_google(audio)  # Recognize the actual command
          processCommand(command)  # Process whatever was spoken

    # Handle any errors during recognition
    except Exception as e:
      print("Error: {0}".format(e))  # Print the exception error message if any occurs
