from splayTree import SplayTree
from storageAndRetrieval import serialize
import json

#build a Splay tree using SplayTree.py
def build():
    data = {}
    #load dataset
    with open('../data/created_data/full_dataset.json', 'r') as dataset:
        data = json.load(dataset)
    #initializing Splay tree
    sTree = SplayTree()
    #inserting into Splay Tree
    for item in data.items():
        sTree.insert(float(item[0]))

    serialize(sTree, 'S')


build()
