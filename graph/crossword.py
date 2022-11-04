#!/usr/bin/env python3
from collections import namedtuple
from itertools import product
from dataclasses import dataclass
from dataclasses import field
from collections import defaultdict

coords = namedtuple("coords",["x","y"])

# Undirected, unweighted graph
class uu_graph:
    def __init__(self, mat):
        self.mat = mat
        self.shape = coords(len(self.mat), len(self.mat[0]))

    def value_get(self, c):
        return self.mat[c.x][c.y]

    def neighbours(self, c):
        tmp = list()
        for i in (-1,0,1):
            for j in (-1,0,1):
                # We don't want to include the same node as its neighbour
                # so 0,0 is not needed
                if not(i == 0 and j == 0):
                    x = c.x+i
                    y = c.y+j
                    # Check for boundaries. We can't use IndexError exception
                    # as python allows negative indices
                    if x in range(0,self.shape.x) and\
                            y in range(0,self.shape.y):
                                tmp.append(coords(x,y))
        return tmp
    
    def __iter__(self):
        for i in range(self.shape.x):
            for j in range(self.shape.y):
                yield coords(i,j)

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

def max_score_words(graph, words, k):
    pq = sorted(words, key=lambda x:len(x))
    ref_dict = defaultdict(list)
    for i in graph:
        ref_dict[graph.value_get(i)].append(i)
    for i in range(k):
        string = pq.pop()
        for j in string:
            print(ref_dict[j])

if __name__ == "__main__":
    rows = int(input())
    cols = int(input())
    mat = list()
    for i in range(rows):
        mat.append(list(input()))
    words = input().split()
    g = uu_graph(mat)
    t = trie()
    for i in words:
        t.insert(i)
    max_score_words(g, words, 1)
