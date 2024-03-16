from helpers.speaking import say
from helpers.transcribe import transcribe
from helpers.recording import recordAudio
from ai.gpt import askGpt
import os

def removeFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Removed file {file_name}")

def main():
    
    say("Welcome to phoneGPT")

    while True:
        try:
            # Record audio from the user's microphone
            recorded_audio_file = recordAudio(max_length_seconds=10)

            # Transcribe the audio to text
            user_input_prompt = transcribe(recorded_audio_file)
            print(f"User input: {user_input_prompt}")

            # Clean up the recorded audio file
            removeFile(recorded_audio_file)

            if (user_input_prompt != None):
                # Send the user's question to chatGPT
                gpt_response = askGpt(user_input_prompt)
                print(f"ChatGPT Response: {gpt_response}")

                # Output the response as audio
                say(gpt_response)

        except KeyboardInterrupt as e:
            print("Shutting down")
            break

        except Exception as e:
            print(f"Something went wrong: {e}")
            break

if __name__ == "__main__":
    main()