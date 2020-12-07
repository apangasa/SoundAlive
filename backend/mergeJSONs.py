import json
import os

OLD_DIR = '../data/created_data/processed_data'
NEW_DIR = '../data/created_data'
combined = {}

for filename in os.listdir(OLD_DIR):
    with open(OLD_DIR + '/' + filename, 'r') as key:
        this_dict = json.load(key)
        print(len(this_dict))
        combined.update(this_dict)

print('Final size: ')
print(len(combined))
with open(NEW_DIR + '/' + 'combined_raw.json', 'w') as combined_key:
    json.dump(combined, combined_key)
