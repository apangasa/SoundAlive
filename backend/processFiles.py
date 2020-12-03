# THIS SCRIPT REQUIRES YOU TO BEGIN WITH A FOLDER OF MP3 FILES

import os
from shutil import copyfile
from pydub import AudioSegment
from scipy.io import wavfile
import csv
import json
import time

DIR = r'../data/Random Sample'  # FILEPATH WHERE MP3s ARE CURRENTLY STORED
MAP = r'../data/0_10000MLFiles.csv'  # FILEPATH TO CSV KEY
FINAL_DIR = r'../data/created_data'

list_dir = os.listdir(DIR)


def trim_wav(wavPath):
    sampleRate, waveData = wavfile.read(wavPath)
    n = waveData.size
    duration = n / sampleRate

    clip_size = 10

    if duration < clip_size:
        clip_size /= 3

    start = (duration - clip_size) / 2
    end = clip_size + ((duration - clip_size) / 2)

    startSample = int(start * sampleRate)
    endSample = int(end * sampleRate)
    wavfile.write(wavPath, sampleRate, waveData[startSample:endSample])


def process_signal(wavPath, animal_name):
    # gives a random number, get rid of this after signal processing is written
    value = int(''.join(str(ord(c)) for c in animal_name))

    # PROCESS SIGNAL HERE @ PRAVEEN

    return value


def rename(path, filename):
    ml_num = filename[0:filename.index('.')]
    ext = filename[filename.index('.'):]
    with open(MAP, 'r') as legend:
        # ln = 0
        reader = csv.reader(legend, delimiter=',')
        for row in reader:
            if str(row[0]) == str(ml_num):
                new_name = str(row[3])
                if '.' in new_name:
                    new_name = new_name.replace('.', ' ', 3)
                new_name = new_name + ext
                if '/' in new_name:
                    new_name = new_name.replace('/', ' ', 3)

                src = path + '/' + filename
                dest = path + '/' + new_name
                copyfile(src, dest)
                os.remove(src)
                return new_name


def process_files():
    value_to_name = {}
    for filename in list_dir:
        try:
            sound = AudioSegment.from_mp3(DIR + '/' + filename)
            filename = filename[0:filename.index('.')]
            sound.export(DIR + '/' + filename + '.wav', format="wav")
            os.remove(DIR + '/' + filename + '.mp3')

            trim_wav(DIR + '/' + filename + '.wav')

            old_filename = filename
            filename = rename(DIR, filename + '.wav')
            if filename is None:
                os.remove(DIR + '/' + old_filename)
                continue

            filename = filename[0:filename.index('.')]

            value = process_signal(DIR + '/' + filename + '.wav', filename)
            os.remove(DIR + '/' + filename + '.wav')

            value_to_name[value] = filename
        except Exception as e:
            print(e)

    return value_to_name


def main():
    t1 = time.time()
    value_to_name = process_files()
    t2 = time.time()

    with open(FINAL_DIR + '/our_key.json', 'w') as our_key:
        json.dump(value_to_name, our_key)

    print('Time taken is ')
    print(str((t2 - t1)))


main()
