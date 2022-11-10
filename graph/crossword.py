#!/usr/bin/env python3
from collections import namedtuple
from itertools import product
from dataclasses import dataclass
from dataclasses import field
from collections import defaultdict
import sys


coords = namedtuple("coords", ["x", "y"])


# Undirected, unweighted graph
class uu_graph:
    def __init__(self, mat):
        self.mat = mat
        self.shape = coords(len(self.mat), len(self.mat[0]))

    def value_get(self, c):
        return self.mat[c.x][c.y]

    def neighbours(self, c):
        tmp = list()
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                # We don't want to include the same node as its neighbour
                # so 0,0 is not needed
                if not (i == 0 and j == 0):
                    x = c.x+i
                    y = c.y+j
                    # Check for boundaries. We can't use IndexError exception
                    # as python allows negative indices
                    if x in range(0, self.shape.x) and\
                            y in range(0, self.shape.y):
                        tmp.append(coords(x, y))
        return tmp

    def search(self, node, string, path):
        # If the string is empty that means we have a path which contains all
        # the characters
        if string:
            if self.value_get(node) == string[0]:
                # We need atleast one neighbour with the next letter
                ret = False
                for i in self.neighbours(node):
                    ret = ret or self.search(i, string[1:], path)
                if ret:
                    path.append(node)
                return ret
            else:
                return False
        else:
            return True

    def __iter__(self):
        for i in range(self.shape.x):
            for j in range(self.shape.y):
                yield coords(i, j)


def max_score_words(graph, ref_dict, words, k):
    pq = sorted(words, key=lambda x: len(x))
    for i in range(k):
        string = pq.pop()
        starts = ref_dict[string[0]]
        for i in starts:
            path = list()
            if graph.search(i, string, path):
                print(f"{string}:{path[::-1]}")


def lpref_words(graph, ref_dict, words, c):
    starts = ref_dict[c]
    for i in words:
        if i.startswith(c):
            for j in starts:
                path = list()
                if graph.search(j, i, path):
                    print(f"{i}:{path[::-1]}")


def ref_dict_create(graph, words):
    ref_dict = defaultdict(list)
    for i in graph:
        ref_dict[graph.value_get(i)].append(i)
    return ref_dict


def usage():
    print('''Usage: crossword K L
    k\t-\tNumber of maximum words needed
    L\t-\tStarting Letter
    INPUT:
    #(ROWS)
    #(COLS)
    GRID
    WORDS
    EXAMPLE INPUT:
    4
    4
    efga
    ...
    she see sees beard''')
    exit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    k = int(sys.argv[1])
    c = sys.argv[2]

    rows = int(input())
    cols = int(input())
    mat = list()
    for i in range(rows):
        mat.append(list(input()))
    words = input().split()

    g = uu_graph(mat)
    ref_dict = ref_dict_create(g, words)

    max_score_words(g, ref_dict, words, k)
    lpref_words(g, ref_dict, words, c)
