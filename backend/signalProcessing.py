import numpy as np
from scipy.io.wavfile import read
import math


def process_signal(wavPath, animal):
    fs, data_raw = read(wavPath)
    data = []
    for i in range(len(data_raw)):
        if data_raw[i] != 0:
            data.append(data_raw[i])
    data = np.array(data)
    w = np.arange(0, (math.pi/2) + (math.pi/20), math.pi/20)
    h = np.zeros(len(w), dtype=complex)
    for x in range(len(w)):
        for k in range(0, len(data), 2):
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
