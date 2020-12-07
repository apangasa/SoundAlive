from bTree import BTree
from splayTree import SplayTree
import pickle
import json
import time
from signalProcessing import process_signal
from pydub import AudioSegment
from processFiles import trim_wav

# tree = BTree(4)

# x = [0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

# for i in range(20):
#     tree.insert(i % 4)

# tree.print_order()

# print(tree.search(1))
# print(tree.search(2))

# with open('../data/created_data/tree.pickle', 'wb') as tree_file:
#     pickle.dump(tree, tree_file)

# tree = None

b, s = None, None

filename = 'SohilSounds'

t1 = time.time()
with open('../data/created_data/B.pickle', 'rb') as tree_file:
    b = pickle.load(tree_file)
    # x.print_order()
t2 = time.time()

print('Time to load B tree')
print(t2 - t1)

t1 = time.time()
with open('../data/created_data/S.pickle', 'rb') as tree_file:
    s = pickle.load(tree_file)
    # x.print_order()
t2 = time.time()

print('Time to load Splay tree')
print(t2 - t1)


t1 = time.time()
# sound = AudioSegment.from_mp3('../data/' + filename + '.mp3')
# filename = filename[0:filename.index('.')]
# sound.export('../data/' + filename + '.wav', format="wav")
# os.remove('/input.mp3')

# trim_wav('../data/' + filename + '.wav')


val = process_signal('../data/' + filename + '.wav', filename)
print(val)
t2 = time.time()

print('Time to process signal')
print(t2 - t1)

t1 = time.time()
bmatches = b.get_matches(val)
print(bmatches)
t2 = time.time()

print('Time to get B matches')
print(t2 - t1)

t1 = time.time()
smatches = s.get_matches(None, val)
print(smatches)
t2 = time.time()

print('Time to get S matches')
print(t2 - t1)

banimals = []
sanimals = []
lookup = {}
with open('../data/created_data/full_dataset.json', 'r') as dataset:
    lookup = json.load(dataset)
    for match in bmatches:
        banimals.append(lookup[str(match)])
    for match in smatches:
        sanimals.append(lookup[str(match)])
print(banimals)
print(sanimals)
