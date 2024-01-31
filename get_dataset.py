import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 3
count = 0

while count < 100:
    print("Say Bang!")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    path = "dataset/ouput%i.wav" % count
    write(path, fs, recording)
    count += 1