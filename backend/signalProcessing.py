import numpy as np
import librosa
import soundfile as sf
from scipy.io.wavfile import read
import wavfile as wvf
import wavio
import math


def process_signal(wavPath, animal):
    # x, _ = librosa.load(wavPath, sr=16000)
    # sf.write(wavPath, x, 16000)

    # ideally use just the following line:
    # fs, data_raw = read(wavPath)
    try:
        fs, data_raw = read(wavPath)
        # fs, data_raw, _ = wvf.read(wavPath)
        data = []
        for i in range(len(data_raw)):
            if data_raw[i] != 0:
                data.append(data_raw[i])
    except:
        #WAV to numpy array
        fs, data_raw = read(wavPath)
        # fs, data_raw, _ = wvf.read(wavPath)
        data_raw = data_raw[:, 0]
        data = []
        #removing parts with no sound
        for i in range(len(data_raw)):
            if data_raw[i] != 0:
                data.append(data_raw[i])
    data = np.array(data)
    #recording frequency in range of 0-pi/2 with 10 intervals
    w = np.arange(0, (math.pi/2) + (math.pi/20), math.pi/20)
    h = np.zeros(len(w), dtype=complex)
    for x in range(len(w)):
        for k in range(0, len(data), 2):
            #calculating frequency response for each freqeuncy interval
            h[x] = h[x] + (data[k] * (math.cos(-1 * w[x] * k) +
                                      1j*math.sin(-1 * w[x] * k)))
    #finding amplitude and maximum frequency spike
    avg_data = np.average(data)
    amp = max(data) - avg_data
    h = np.abs(h)
    avg_h = np.average(h)
    for i in range(len(h)):
        if h[i] > avg_h:
            index = i
    freq = abs(w[index])
    #value for input in trees
    output = amp * freq
    return output
