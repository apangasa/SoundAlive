# THIS SCRIPT IS FOR PROCESSING FILES AS DATA IS REQUESTED
# FILES WILL BE DELETED AS THEY ARE PROCESSED

import os
from shutil import copyfile
from pydub import AudioSegment
from scipy.io import wavfile
import requests
import csv
import json
import time

from processFiles import trim_wav, rename, process_signal

DIR = r'../data/Random Sample'  # FILEPATH TO SAVE TEMP FILES
MAP = r'../data/0_10000MLFiles.csv'  # FILEPATH TO CSV KEY
FINAL_DIR = r'../data/created_data'
POINTS_PER_TEN_THOUSAND = 1


def request_data(index):
    url = 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/' + \
        str(index)
    filedata = requests.get(url)
    if filedata.headers.get('content-type') == 'audio/mpeg':
        with open(DIR + '/' + str(index) + '.mp3', 'wb') as f:
            f.write(filedata.content)
    else:
        print(index)
        print('Invalid Request')
        raise Exception('Invalid request')


def process_data(index):

    try:
        sound = AudioSegment.from_mp3(DIR + '/' + str(index) + '.mp3')
        sound.export(DIR + '/' + str(index) + '.wav', format="wav")
        os.remove(DIR + '/' + str(index) + '.mp3')

        trim_wav(DIR + '/' + str(index) + '.wav')

        filename = rename(DIR, str(index) + '.wav')
        if filename is None:
            os.remove(DIR + '/' + str(index) + '.wav')
            return None, None

        filename = filename[0:filename.index('.')]

        value = process_signal(DIR + '/' + filename + '.wav', filename)
        os.remove(DIR + '/' + filename + '.wav')

        return (value, filename)
    except Exception as e:
        print(e)
        print(index)
        try:
            os.remove(DIR + '/' + str(index) + '.mp3')
        except:
            pass
    return None, None


def main():
    index = 0
    count = 0
    value_to_name = {}

    t1 = time.time()
    while count < POINTS_PER_TEN_THOUSAND * 5:
        print(count)
        try:
            # REQUEST AND SAVE DATA
            request_data(index)
            # PROCESS DATA
            (value, filename) = process_data(index)
            if value is None or filename is None:
                index += 1
                continue
            # APPEND TO DICT
            value_to_name[value] = filename
            # REGISTER THAT A DATA POINT WAS ACTUALLY RECEIVED
            count += 1
            print(count)
            if count % POINTS_PER_TEN_THOUSAND == 0:
                index += (10000 - POINTS_PER_TEN_THOUSAND)
                with open(FINAL_DIR + '/our_key_2.json', 'w') as our_key:
                    json.dump(value_to_name, our_key)
            else:
                index += 1
        except:
            index += 1

    t2 = time.time()

    with open(FINAL_DIR + '/our_key_2.json', 'w') as our_key:
        json.dump(value_to_name, our_key)

    print('Time taken is ')
    print(str((t2 - t1)))


main()
