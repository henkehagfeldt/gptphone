import pyttsx3

engine = pyttsx3.init()

def say(prompt):
    print(f"Saying {prompt}")
    engine.say(prompt)
    engine.runAndWait()