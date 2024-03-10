from gtts import gTTS
from io import BytesIO

# This module is imported so that we can  
# play the converted audio 
import subprocess

def say(prompt):

    tts = gTTS(text=prompt, lang="en")
    
    # convert to file-like object
    fp = BytesIO()
    tts.save("response.mp3")
    #fp.seek(0)

    subprocess.call(["cvlc", "response.mp3"])