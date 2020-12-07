import json

x = None
with open('../data/created_data/full_dataset.json', 'r') as f:
    x = json.load(f)

l = []
for key in x.keys():
    l.append(float(key))

print(min(l))
l.remove(0.0)
print(min(l))
print(max(l))
