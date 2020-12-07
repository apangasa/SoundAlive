import pickle


def serialize(tree, name):
    with open('../data/created_data/' + name + '.pickle', 'wb') as tree_file:
        pickle.dump(tree, tree_file)


def deserialize():
    b_tree = None
    s_tree = None
    with open('../data/created_data/B.pickle', 'rb') as tree_file:
        b_tree = pickle.load(tree_file)
    with open('../data/created_data/S.pickle', 'rb') as tree_file:
        s_tree = pickle.load(tree_file)
    return (b_tree, s_tree)
