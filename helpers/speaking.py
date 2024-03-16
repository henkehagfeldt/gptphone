from gtts import gTTS
from pygame import mixer  # Load the popular external library
from helpers.utils import removeFile
import time

save_file = "response.mp3"

def say(prompt):

    tts = gTTS(text=prompt, lang="en")
    tts.save(save_file) 

    mixer.init()
    mixer.music.load(save_file)
    mixer.music.play()

    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)
    
    #removeFile(save_file)