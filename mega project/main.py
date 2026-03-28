import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import time


recognizer = sr.Recognizer()
newsapi = "782fef2cab454242aac815108e7746b5"
weatherapi = "c185f11bb4ab4b338bb113817252412"

def speak(text):
    try:
        local_engine = pyttsx3.init()
        local_engine.say(text)
        local_engine.runAndWait()
        try:
            local_engine.stop()
        except Exception:
            pass
    except Exception as e:
        print("TTS error:", e)


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link) 
    elif "weather" in c.lower():
        # Example command: "Friday, tell me the weather in New York"
        try:
            # This splits the command to find the city name after "weather in"
            if "weather in" in c.lower():
                city = c.lower().split("weather in")[1].strip()
            else:
                # Default to a specific city if user just says "weather" (Optional)
                speak("Which city?")
                return 

            url = f"https://api.weatherapi.com/v1/current.json?key=c185f11bb4ab4b338bb113817252412&q=London&aqi=yes"
            r = requests.get(url)
            
            if r.status_code == 200:
                data = r.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}")
            else:
                speak(f"Sorry, I couldn't find weather information for {city}")
        except Exception as e:
            speak("Sorry, there was an error getting the weather.")
            print(e)
            
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the json response
            data = r.json()
            # Extract the articles
            articles = data.get('articles', [])
            # print the headlines
            for article in articles:
                speak(article['title'])
       

if __name__ == "__main__":
    speak("Initializing Friday...")
    while True:
        # Listen for the wake word "Friday"
        # obtain audion from the microphone
        r = sr.Recognizer()
       
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            print("recognizing...")
            word = r.recognize_google(audio)
            if "friday" in word.lower():
                speak("Hi prakshil ,How may I help you")
                # Give TTS a moment to finish so microphone doesn't capture it
                time.sleep(1.0)
                # listen for command
                with sr.Microphone() as source:
                    print("Friday active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))