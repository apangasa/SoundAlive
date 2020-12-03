import random
import json

one_copy_dict = {}
with open('our_key_2.json', 'r') as our_key:
    one_copy_dict = json.load(our_key)

multi_copy_dict = {}
for item in one_copy_dict.items():
    animal = item[1]
    multi_copy_dict[item[0]] = animal
    for i in range(len(14)):
        x = random.uniform(-18.0, 18.0)
        new_val = item[0] + x
        multi_copy_dict[new_val] = animal


with open('our_key_3.json', 'w') as our_key:
    json.dump(multi_copy_dict, our_key)
