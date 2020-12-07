from splayTree import SplayTree
from storageAndRetrieval import serialize
import json


def build():
    data = {}
    with open('../data/created_data/full_dataset.json', 'r') as dataset:
        data = json.load(dataset)

    sTree = SplayTree()

    for item in data.items():
        sTree.insert(float(item[0]))

    serialize(sTree, 'S')


build()
