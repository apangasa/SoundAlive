import json

x = None
#load up dataset from json
with open('../data/created_data/full_dataset.json', 'r') as f:
    x = json.load(f)

l = []
#add all items into python dictionary
for key in x.keys():
    l.append(float(key))

print(min(l))
l.remove(0.0)
print(min(l))
print(max(l))
