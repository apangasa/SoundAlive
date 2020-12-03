from bTree import BTree


tree = BTree(4)

for i in range(100000):
    tree.insert(pow(i, 4) % 567)

tree.print_order()

print(tree.search(1))
print(tree.search(2))
