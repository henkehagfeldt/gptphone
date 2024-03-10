from gtts import gTTS
import pygame
from io import BytesIO

# This module is imported so that we can  
# play the converted audio 
import os 

def say(prompt):

    tts = gTTS(text=prompt, lang="en")
    
    # convert to file-like object
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)