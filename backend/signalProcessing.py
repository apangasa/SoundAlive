import numpy as np
from scipy.io import wavfile
import math


def process_signal(wavPath, animal):
    fs, data = wavfile.read(wavPath)
    #data = data[(len(data)//2):]
    for i in range(len(data)):
        if data[i] == 0:
            np.delete(data, i)
    w = np.arange(-1 * math.pi, math.pi + (math.pi/10), math.pi/10)
    h = np.zeros(len(w), dtype=complex)
    for x in range(len(w)):
        for k in range(len(data)):
            h[x] = h[x] + (data[k] * (math.cos(-1 * w[x] * k) +
                                      1j*math.sin(-1 * w[x] * k)))
    avg_data = np.average(data)
    amp = max(data) - avg_data
    h = np.abs(h)
    avg_h = np.average(h)
    for i in range(len(h)):
        if h[i] > avg_h:
            index = i
    freq = abs(w[index])
    output = amp * freq
    return output
