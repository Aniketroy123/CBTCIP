#Task 3

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
freq = 44100
duration = 10
recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)

sd.wait()
write("scipy_rec.wav", freq, recording)
wv.write("wavio_rec.wav", recording, freq, sampwidth=2)


