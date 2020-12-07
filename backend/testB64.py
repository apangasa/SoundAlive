import config

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests
import time
import os
import base64

# from classDefs import BTree, Splay
from bTree import BTree
from storageAndRetrieval import deserialize, serialize
from signalProcessing import process_signal
from identifyAnimals import get_matches
from pydub import AudioSegment


(b_tree, splay_tree) = deserialize()
content = config.base64img  # request.json.get('content', None)
# content = request.get_data()
# print('hi')
# file = request.files['file']
# print('hello')
# print(file)
# filename = 'input.mp3'
# file.save('/input.mp3')

print('Content is')
print(content)

x = 'data:audio/mp3;base64,//'

content = content.split(',')[1]

if not content:
    # return 'No content provided', 400
    pass

decoded = base64.b64decode(content + '===')

try:
    with open('../data/input.wav', 'wb') as f:
        f.write(decoded)
except Exception as e:
    print(e)

# sound = AudioSegment.from_mp3('../data/input.mp3')
# # filename = filename[0:filename.index('.')]
# sound.export('../data/input.wav', format="wav")
# # os.remove('/input.mp3')

val = process_signal('../data/input.wav', 'input')
# v = val[0]

if not val:
    # return 'No audio provided', 400
    pass

t1 = time.time()
b_matches = b_tree.get_matches(val)
print(b_matches)
b_animals = []
lookup = {}
with open('../data/created_data/full_dataset.json', 'r') as dataset:
    lookup = json.load(dataset)
    for match in b_matches:
        b_animals.append(lookup[str(match)])
print(b_animals)
t2 = time.time()

# t3 = time.time()
# s_matches = get_matches(splay_tree, val)
# t4 = time.time()

serialize(b_tree, 'B')
serialize(splay_tree, 'S')

results = {
    'B': {
        'matches': b_animals,
        'time': t2 - t1
    },
    # 'Splay': {
    #     'matches': s_matches,
    #     'time': t4 - t3
    # },
    'Value': val
}

print(val)
