from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import csv
# import requests
import time
import os
import base64

# from classDefs import BTree, Splay
from bTree import BTree
from splayTree import SplayTree
from storageAndRetrieval import deserialize, serialize
from signalProcessing import process_signal
from writeToCSV import to_csv
# from identifyAnimals import get_matches
# from pydub import AudioSegment


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def helloWorld():
    return 'This application is up and running!', 200


@app.route('/process-audio', methods=['POST'])
def processAudio():
    (b_tree, splay_tree) = deserialize()
    # receive base 64 of uploaded wav file
    content = request.json.get('content', None)
    filename = request.json.get('filename', None)
    # content = request.get_data()
    # print('hi')
    # file = request.files['file']
    # print('hello')
    # print(file)
    # filename = 'input.mp3'
    # file.save('/input.mp3')

    print('Content is')
    # print(content)

    content = content.split(',')[1]  # get rid of prefix in base 64

    if not content:
        return 'No content provided', 400

    # decode the base 64 string into bytestream
    decoded = base64.b64decode(content)

    try:
        with open('../data/input.wav', 'wb') as f:
            f.write(decoded)  # write the bytestream to a wav file
    except Exception as e:
        print(e)
        return 'Could not write to file', 400

    # sound = AudioSegment.from_mp3('../data/input.mp3')
    # # filename = filename[0:filename.index('.')]
    # sound.export('../data/input.wav', format="wav")
    # # os.remove('/input.mp3')

    # process the signal from the sent file
    val = process_signal('../data/input.wav', 'input')
    # v = val[0]

    if not val:
        return 'Audio could not be analyzed', 400

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

    t3 = time.time()
    # pass None as first param to indicate that there is no parent to the tree
    s_matches = splay_tree.get_matches(None, val)
    print(s_matches)
    s_animals = []
    lookup = {}
    with open('../data/created_data/full_dataset.json', 'r') as dataset:
        lookup = json.load(dataset)
        for match in s_matches:
            s_animals.append(lookup[str(match)])
    print(s_animals)
    t4 = time.time()

    serialize(b_tree, 'B')
    serialize(splay_tree, 'S')

    to_csv(filename, b_animals, s_animals, t2 - t1, t4 - t3)

    results = {
        'B': {
            'matches': b_animals,
            'time': t2 - t1
        },
        'Splay': {
            'matches': s_animals,
            'time': t4 - t3
        },
        'Value': val
    }

    print(val)

    return jsonify(results), 200


# if __name__ == '__main__':
#     app.run()
