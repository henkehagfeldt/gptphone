import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Attempt to transcribe the audio read from the audio file.
# If the audio can not be transcribed, will return None
def transcribe(fileName):

    # Load the audio file
    with sr.AudioFile(fileName) as source:
        audio_data = recognizer.record(source)

    # Use the Google Web Speech API to transcribe the audio
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))