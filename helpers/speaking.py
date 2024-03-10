#import pyttsx3

#engine = pyttsx3.init()

#def say(prompt):
#    print(f"Saying {prompt}")
#    engine.say(prompt)
#    engine.runAndWait()

from gtts import gTTS

# This module is imported so that we can  
# play the converted audio 
import os 

def say(prompt):

    # Language in which you want to convert 
    language = 'en'

    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=prompt, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 

    # Playing the converted file 
    os.system("aplay welcome.mp3") 