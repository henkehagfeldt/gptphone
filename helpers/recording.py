import pyaudio
import wave
import audioop

# Static Parameters
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate
CHUNK = 1024  # Frame size
SILENCE_THRESHOLD = 1000  # Threshold for detecting silence, adjust based on your mic
SILENCE_DURATION = 2  # How many seconds of silence before stopping

# Function to detect silence
def is_silent(data_chunk):
    """Determine if the given audio chunk is silent."""
    rms = audioop.rms(data_chunk, 2)  # Get the root mean square of the chunk
    return rms < SILENCE_THRESHOLD

def streamAudio(audio, length):
    # Start the recording process
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    silent_chunks = 0
    total_duration = 0
    first_chunk = True

    while total_duration < length:
        data = stream.read(CHUNK)
        frames.append(data)

        currently_silent = is_silent(data)

        # Check for silence to stop recording, unless waiting for first sound
        if currently_silent and not first_chunk:
            silent_chunks += 1
            silence_sec = (silent_chunks * CHUNK) / RATE
            if silence_sec >= SILENCE_DURATION:
                print("Stopped recording due to silence.")
                break
        elif not currently_silent:
            silent_chunks = 0
            first_chunk = False
            print("Detected Audio!")

        total_duration += CHUNK / RATE

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Return the recorded frames
    return frames

def saveAudio(audio_frames, audio_sample_size, file_name):
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio_sample_size)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(audio_frames))
    wf.close()

def recordAudio(output_file_name="recording.wav", max_length_seconds=5):

    audio = pyaudio.PyAudio()
    
    # Configurable Parameters
    RECORD_SECONDS = max_length_seconds  # Maximum duration of recording
    WAVE_OUTPUT_FILENAME = output_file_name  # Output file
    
    # Record audio from mic
    print("Recording...")
    recorded_frames = streamAudio(audio, RECORD_SECONDS)

    # Save the recorded data as a WAV file
    saveAudio(audio_frames=recorded_frames, 
            audio_sample_size=audio.get_sample_size(FORMAT), 
            file_name=WAVE_OUTPUT_FILENAME)
    
    # Return the path of the recorded file
    return output_file_name
