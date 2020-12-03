import random
import json

COPIES = 14

one_copy_dict = {}
with open('../data/created_data/our_key_2.json', 'r') as our_key:
    one_copy_dict = json.load(our_key)

print(len(one_copy_dict))

multi_copy_dict = {}
for item in one_copy_dict.items():
    animal = item[1]
    multi_copy_dict[item[0]] = animal
    for i in range(COPIES):
        x = random.uniform(-18.0, 18.0)
        new_val = float(item[0]) + x
        multi_copy_dict[str(new_val)] = animal

print(len(multi_copy_dict))

with open('../data/created_data/our_key_3.json', 'w') as our_key:
    json.dump(multi_copy_dict, our_key)
