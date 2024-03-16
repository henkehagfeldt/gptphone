from gtts import gTTS
from io import BytesIO
import pygame

initialized = False

def init():
    if not initialized:
        pygame.init()
        initialized = True

def say(prompt):

    mp3_file_object = BytesIO()
    tts = gTTS(text=prompt, lang="en")
    tts.write_to_fp(mp3_file_object)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file_object, 'mp3')
    pygame.mixer.music.play()
