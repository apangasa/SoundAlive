import random
import json

MIN_COPIES_PER_ANIMAL = 50
#creating copies of animals with slight variation in dataset
one_copy_dict = {}
with open('../data/created_data/combined_raw.json', 'r') as our_key:
    one_copy_dict = json.load(our_key)

print('Initial data size')
print(len(one_copy_dict))

copied = {''}
copied.remove('')
#for each item, if not copied, add respective amounts of animals (if not enough animals) or remove animals if too many animals
multi_copy_dict = {}
for item in one_copy_dict.items():
    animal = item[1]
    multi_copy_dict[item[0]] = animal
    #if correct number of copied animals continue
    if animal in copied:
        continue

    instances = sum(i == animal for i in one_copy_dict.values())
    # print(instances)

    copies = 0
    #If not enough animals, generate copies of animals or destroy extra copies
    if instances > MIN_COPIES_PER_ANIMAL:
        copied.add(animal)
        print(animal + ' ' + str(instances))
        continue
    else:
        copies = MIN_COPIES_PER_ANIMAL - instances

    for i in range(copies):
        #randomizing copies with slight variation
        x = random.uniform(-18.0, 18.0)
        new_val = float(item[0]) + x
        multi_copy_dict[str(new_val)] = animal

    copied.add(animal)

print('Full dataset size')
print(len(multi_copy_dict))

#Writing new dataset to file
with open('../data/created_data/full_dataset.json', 'w') as our_key:
    json.dump(multi_copy_dict, our_key)

print('Number of distinct animals')
print(len(copied))
