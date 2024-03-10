from gtts import gTTS
from io import BytesIO
import simpleaudio as sa

# This module is imported so that we can  
# play the converted audio 
import subprocess

def say(prompt):

    tts = gTTS(text=prompt, lang="en")
    
    # convert to file-like object
    fp = BytesIO()
    tts.save("response.mp3")
    #fp.seek(0)

    subprocess.call(["vlc", "response.mp3"])

    play_audio(fp)

def play_audio(fp):
    fp.seek(0)
    audio_data = fp.read()
    wave_obj = sa.WaveObject(audio_data, num_channels=2, bytes_per_sample=2, sample_rate=44100)
    play_obj = wave_obj.play()
    play_obj.wait_done()