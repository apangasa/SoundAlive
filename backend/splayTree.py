class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

    def get_matches(self, parent, payload):  # parent will be None in initial call
        if self == None:
            # handle via parent
            matches = []
            matches.append(parent.key)
            # self.splay(parent.key)
            return matches
        if self.key == payload:
            # handle
            matches = []
            matches.append(self.key)
            if(self.left and self.right and parent):
                # both children and parent are present, choose closest
                dLeft = abs(self.left.key - payload)
                dRight = abs(self.right.key - payload)
                dParent = abs(parent.key - payload)
                possibleFarthestKey1 = max(dLeft, dRight, dParent) + payload
                possibleFarthestKey2 = max(dLeft, dRight, dParent) - payload

                matches.append(self.left.key)
                matches.append(self.right.key)
                matches.append(parent.key)

                try:
                    matches.remove(possibleFarthestKey1)
                    # for match in matches:
                    #     self.splay(match)
                    return matches
                except:
                    try:
                        matches.remove(possibleFarthestKey2)
                        # for match in matches:
                        #     self.splay(match)
                        return matches
                    except:
                        # for match in matches:
                        #     self.splay(match)
                        return matches
            elif(self.left and parent):
                matches.append(self.left.key)
                matches.append(parent.key)
                return matches
            elif(self.right and parent):
                matches.append(self.right.key)
                matches.append(parent.key)
                return matches
            elif(self.left and self.right):
                matches.append(self.left. key)
                matches.append(self.right.key)
                return matches
            elif(not self.left and not self.right and parent):
                matches.append(parent)
                return matches
        elif self.key < payload:
            if self.right:
                matches = self.right.get_matches(self, payload)
                if matches is not None:
                    if len(matches) < 3:
                        matches.append(self.key)
                        # self.splay(self.key)
                        return matches
                    else:
                        return matches
                else:
                    return []
            else:
                return [self.key]
        else:
            if self.left:
                matches = self.left.get_matches(self, payload)
                if matches is not None:
                    if len(matches) < 3:
                        matches.append(self.key)
                        # self.splay(self.root.key)
                        return matches
                    else:
                        return matches
                else:
                    return []
            else:
                return [self.key]


class SplayTree:
    def __init__(self):
        self.root = None
        self.header = SplayNode(None)  # For splay()

    def get_matches(self, parent, payload):  # parent will be None in initial call
        if self.root == None:
            # handle via parent
            matches = []
            matches.append(parent.key)
            self.splay(parent.key)
            return matches
        if self.root.key == payload:
            # handle
            matches = []
            matches.append(self.root.key)
            if(self.root.left and self.root.right and parent):
                # both children and parent are present, choose closest
                dLeft = abs(self.root.left.key - payload)
                dRight = abs(self.root.right.key - payload)
                dParent = abs(parent.key - payload)
                possibleFarthestKey1 = max(dLeft, dRight, dParent) + payload
                possibleFarthestKey2 = max(dLeft, dRight, dParent) - payload

                matches.append(self.root.left.key)
                matches.append(self.root.right.key)
                matches.append(parent.key)

                try:
                    matches.remove(possibleFarthestKey1)
                    for match in matches:
                        self.splay(match)
                    return matches
                except:
                    try:
                        matches.remove(possibleFarthestKey2)
                        for match in matches:
                            self.splay(match)
                        return matches
                    except:
                        for match in matches:
                            self.splay(match)
                        return matches
            elif(self.root.left and parent):
                matches.append(self.root.left.key)
                matches.append(parent.key)
                return matches
            elif(self.root.right and parent):
                matches.append(self.root.right.key)
                matches.append(parent.key)
                return matches
            elif(self.root.left and self.root.right):
                matches.append(self.root.left.key)
                matches.append(self.root.right.key)
                return matches
            elif(not self.root.left and not self.root.right and parent):
                matches.append(parent)
                return matches
        elif self.root.key < payload:
            if self.root.right:
                matches = self.root.right.get_matches(self.root, payload)
                if matches is not None:
                    if len(matches) < 3:
                        matches.append(self.root.key)
                        self.splay(self.root.key)
                        return matches
                    else:
                        return matches
                else:
                    return []
            else:
                return [self.root.key]
        else:
            if self.root.left:
                matches = self.root.left.get_matches(self.root, payload)
                if matches is not None:
                    if len(matches) < 3:
                        matches.append(self.root.key)
                        self.splay(self.root.key)
                        return matches
                    else:
                        return matches
                else:
                    return []
            else:
                return [self.root.key]

    def insert(self, key):
        if (self.root == None):
            self.root = SplayNode(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = SplayNode(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise 'key not found in tree'

        # Now delete the root.
        if self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None

    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
