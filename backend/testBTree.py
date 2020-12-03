from bTree import BTree
import pickle


tree = BTree(4)

x = [0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

for i in range(20):
    tree.insert(i % 4)

tree.print_order()

print(tree.search(1))
print(tree.search(2))

with open('../data/created_data/tree.pickle', 'wb') as tree_file:
    pickle.dump(tree, tree_file)

tree = None


with open('../data/created_data/tree.pickle', 'rb') as tree_file:
    x = pickle.load(tree_file)
    x.print_order()
