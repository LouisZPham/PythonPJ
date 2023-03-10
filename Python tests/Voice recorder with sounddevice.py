import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

# Set the audio parameters
duration = 5  # seconds
fs = 44100  # sample rate

# Record audio
print('Recording audio...')
audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)

# Wait for recording to finish
sd.wait()

# Save audio to a WAV file
write('output.wav', fs, audio)

print('Finished recording audio.')
''' or We can make a function like this

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")
    
'''