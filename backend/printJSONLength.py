import json

x = {}
#print the length of json to identify dataset length
with open('../data/created_data/processed_data/our_key_2.json', 'r') as key:
    x = json.load(key)
    print(len(x))
