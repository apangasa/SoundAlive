from flask import Flask, jsonify, request
import json
import requests
import time

from classDefs import BTree, Splay
from storageAndRetrieval import deserialize, serialize
from signalProcessing import process_signal
from identifyAnimals import get_matches

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloWorld():
    return 'This application is up and running!', 200


@app.route('/process-audio', methods=['POST'])
def processAudio():
    (b_tree, splay_tree) = deserialize()

    # unsure how input will be passed
    val = process_signal(request.json.get('audio', None))

    if not val:
        return 'No audio provided', 400

    t1 = time.time()
    b_matches = get_matches(b_tree, val)
    t2 = time.time()

    t3 = time.time()
    s_matches = get_matches(splay_tree, val)
    t4 = time.time()

    serialize(b_tree)
    serialize(splay_tree)

    results = {
        'B': {
            'matches': b_matches,
            'time': t2 - t1
        },
        'Splay': {
            'matches': s_matches,
            'time': t4 - t3
        }
    }

    return results, 200


if __name__ == '__main__':
    app.run()
