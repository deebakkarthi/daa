#!/usr/bin/env python3


@dataclass
class trienode:
    children: dict = field(default_factory=dict)
    end: bool = False

# Trie to store the words
class trie:
    def __init__(self):
        self.root = None

    def new_node(self):
        return {"childre"}

    def edge_get(self, u, v):
        tmp = self.neighbours(u)
        if v in tmp:
            return True
        return False

    def insert(self, string):
        # Empty trie
        if self.root is None:
            self.root = trienode()
        curr = self.root
        for i in string:
            # The character is not in the trie
            if curr.children.get(i) is None:
                curr.children[i] = trienode()
            curr = curr.children[i]
        # String already in the trie
        if curr.end:
            return False
        else:
            curr.end = True
            return True

    def search(self, string):
        curr = self.root
        for i in string:
            if curr.children.get(i) is None:
                return False
            curr = curr.children[i]
        # If the current node is terminal then the string is there
        return curr.end
        
    def words_get(self, node, prefix, arr):
        if node.end:
            arr.append(prefix)
        for k, v in node.children.items():
            self.words_get(v, prefix+k, arr)


    def __repr__(self):
        arr = list()
        self.words_get(self.root,"",arr)
        return str(arr)
