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

    os.environ['SDL_AUDIODRIVER'] = 'alsa'
    
    pygame.init()
    pygame.mixer.init()

    # Get the audio configuration
    audio_config = pygame.mixer.get_init()
    pygame.mixer.music.set_volume(1.0)  # Set volume to maximum

    # Print the audio configuration
    print("Audio Configuration:")
    print(f"   Audio Device: {audio_config[1]}")
    print(f"   Sample Rate: {audio_config[0]} Hz")
    print(f"   Audio Format: {audio_config[2]}")
    print(f"   Channels: {audio_config[3]}")

    # Initialize the mixer with the specific audio configuration
    pygame.mixer.init(frequency=44100, size=-16, channels=2)

    # Load and play the audio file
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    # Wait for the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)