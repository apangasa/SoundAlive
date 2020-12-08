from bTree import BTree
from storageAndRetrieval import serialize
import json

#Creates a B Tree, using bTree.py file
def build(t):
    data = {}
    #load dataset
    with open('../data/created_data/full_dataset.json', 'r') as dataset:
        data = json.load(dataset)
    #initializing b tree
    bTree = BTree(t)
    #inserting into b tree
    for item in data.items():
        bTree.insert(float(item[0]))

    serialize(bTree, 'B')


build(400)
