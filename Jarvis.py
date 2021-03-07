import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import random
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Good Morning Sir, how are you doing")
    elif time > 12 and time < 18:
        speak("Good Afternoon Sir, how are you doing")
    else:
        speak("Good Evening Sir, how are you doing")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"


if __name__ == "__main__":
    stay = True
    Wishme()
    speak("I am Jarvis, how may I help you Sir?")
    while(stay):
        query = takeCommand()
        print(f"You said this: {query}")
        query = query.lower()
        if "shutdown" or "shut down" in query:
            speak("Bye sir, take care!")
            stay = False
        elif "what can you do" in query:
            speak("Sir, I can open google or youtube or prime videos for you")
            speak("I can also do a wikipedia search of whatever you want..")
            speak("Also I can tell you a joke")
            speak("No sir i am joking")
        elif "google" in query:
            speak("Ok sir, opening google")
            webbrowser.open("google.com")
        elif "youtube" in query:
            speak("Ok sir, opening YouTube")
            webbrowser.open("youtube.com")
        if "prime video" in query:
            speak("Ok sir, opening Amazon Prime video")
            webbrowser.open(
                "https://www.primevideo.com/region/eu/storefront/home/ref=atv_nb_sf_hm")
        elif "wikipedia" in query:
            query = query.replace('wikipedia', '')
            speak(f"Sir, Searching for {query} on wikipedia...")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "joke" in query:
            speak("Ok sir, I hope you find this funny!")
            x = random.randint(0, 4)
            if x == 0:
                speak("Want to hear a construction joke?")
                speak("Oh never mind, I'm still working on that one.")
            elif x == 1:
                speak("Why did the gym close down?")
                speak("It just didn't work out!")
            elif x == 2:
                speak(
                    "I have many jokes about unemployed people, sadly none of them work.")
            elif x == 3:
                speak(
                    "A Buddhist walks up to a hotdog stand and says, Make me one with everything.")
            else:
                speak("How do you keep an idiot in suspense?")
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"Sir, now the time is")
            speak(time)
        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            i = random.randint(0, len(songs) - 1)
            speak("Ok Sir, Starting a song...")
            os.startfile(os.path.join(music_dir, songs[i]))
        elif "fact" in query:
            speak("Ok sir, I hope you find this Interesting!")
            x = random.randint(0, 4)
            if x == 0:
                speak("An ostrich's eye is bigger than its brain.")
            elif x == 1:
                speak(
                    "THE TERM ASTRONAUT COMES FROM GREEK WORDS THAT MEAN STAR AND SAILOR.")
            elif x == 2:
                speak(
                    "SCIENTISTS SAY THAT THE BEST TIME TO TAKE A NAP IS BETWEEN 1 P.M. AND 2:30 P.M. BECAUSE THAT'S WHEN A DIP IN BODY TEMPERATURE MAKES US FEEL SLEEPY.")
            elif x == 3:
                speak(
                    "BECAUSE THE SPEED OF EARTH'S ROTATION CHANGES OVER TIME, A DAY IN THE AGE OF DINOSAURS WAS JUST 23 HOURS LONG.")
            else:
                speak(
                    "THE TV REMOTE IS THE DIRTIEST ITEM IN A TYPICAL HOUSEHOLD, HOSPITAL, OR HOTEL ROOM.")
