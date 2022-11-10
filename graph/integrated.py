#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import chain


class uu_graph:
    def __init__(self):
        self.map = defaultdict(set)
        self.colormap = dict()
        # storing whether a node is integrated or not
        # Useful in ghetto finding
        self.integmap = dict()

    def node_add(self, node, color):
        self.colormap[node] = color

    def edge_add(self, u, v):
        self.map[u].add(v)
        self.map[v].add(u)

    def neighbours(self, node):
        return self.map[node]

    def node_integrated_check(self, node):
        count = defaultdict(int)
        for i in self.neighbours(node):
            count[self.colormap[i]] += 1
        if self.colormap[node] == "B":
            # Atleast as many white neighbours as black
            return count["W"] >= count["B"]
        else:
            # Atleast as many black neighbours as white
            return count["B"] >= count["W"]

    def graph_integrated_check(self):
        for i in self:
            if not self.node_integrated_check(i):
                return False
        return True

    def integmap_create(self):
        for i in self:
            self.integmap[i] = self.node_integrated_check(i)

    def same_color(self, u, v):
        return self.colormap[u] == self.colormap[v]

    def ghetto_get(self):
        self.integmap_create()
        ghetto = list()
        for i in self:
            if not self.integmap[i]:
                # If it is already part of a ghetto, skip
                if i not in set(chain.from_iterable(ghetto)):
                    path = set()
                    self.dfs(i, path)
                    # Should atleast be 3 nodes
                    if len(path) >= 3:
                        ghetto.append(path)
        return ghetto

    def dfs(self, node, path):
        path.add(node)
        for i in self.neighbours(node):
            # ghetto condition
            if not self.integmap[i] and self.same_color(node, i):
                if i not in path:
                    path.add(i)
                    self.dfs(i, path)

    def __iter__(self):
        for i in self.map:
            yield i


def usage():
    print('''Usage: integrated FILE
    Example file format:
    0 W
    1 B
    2 W
    [Edges]
    1 2
    0 2''')
    exit()


def file_to_graph(g, file):
    with open(file, "r") as f:
        line = f.readline()
        while line != "[Edges]":
            line = line.split()
            line[0] = int(line[0])
            g.node_add(*line)
            line = f.readline()
            # Removes the trailing "\n" which allows the comparison
            line = line.strip()
        # Currently line has "[Edges]". So get the first edge
        line = f.readline()
        while line:
            line = line.split()
            line = [int(x) for x in line]
            g.edge_add(*line)
            line = f.readline()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    g = uu_graph()
    file_to_graph(g, sys.argv[1])
    for i in g:
        print(i, g.node_integrated_check(i))
    print("Integrated Graph:", g.graph_integrated_check())
    print("Ghettos:")
    for i in g.ghetto_get():
        print(",".join([f"{x}[{g.colormap[x]}]" for x in i]))
