from gtts import gTTS
import os

def say(prompt):
    tts = gTTS(text=prompt, lang="en")
    tts.save("response.mp3") 
    os.system("afplay response.mp3")
    