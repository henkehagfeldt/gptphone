from gtts import gTTS
from pygame import mixer  # Load the popular external library
import time

def say(prompt):
    tts = gTTS(text=prompt, lang="en")
    tts.save("response.mp3") 

    mixer.init()
    mixer.music.load("response.mp3")
    mixer.music.play()

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)