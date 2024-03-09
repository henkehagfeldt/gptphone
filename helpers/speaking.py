import pyttsx3

engine = pyttsx3.init()

def say(prompt):
    engine.say(prompt)
    engine.runAndWait()