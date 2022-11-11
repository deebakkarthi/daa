#!/usr/bin/env python3
import random
from collections import defaultdict
import sys
import matplotlib.pyplot as plt


class uu_graph:
    def __init__(self):
        self.map = defaultdict(lambda: {"left": [], "right": []})

    def __len__(self):
        return len(self.map)

    def graph_construct(self, edgelist):
        for i in edgelist:
            (u, v, d) = i
            if d == "l":
                if v not in self.map[u]["right"]:
                    self.map[u]["right"].append(v)
                if u not in self.map[v]["left"]:
                    self.map[v]["left"].append(u)
            else:
                if u not in self.map[v]["right"]:
                    self.map[v]["right"].append(u)
                if v not in self.map[u]["left"]:
                    self.map[u]["left"].append(v)

    def __iter__(self):
        for i in self.map:
            yield i


def topo(graph):
    indegree = dict()
    ready = list()
    vis = dict()
    path = list()
    sequences = list()
    for i in graph:
        vis[i] = False
        indegree[i] = len(graph.map[i]["left"])
    topo_rec(graph, indegree, vis, path, sequences)
    return sequences


def topo_rec(graph, indegree, vis, path, sequences):
    for i in graph:
        if indegree[i] == 0 and not vis[i]:
            for j in graph.map[i]["right"]:
                indegree[j] -= 1
            path.append(i)
            vis[i] = True
            topo_rec(graph, indegree, vis, path, sequences)
            for j in graph.map[i]["right"]:
                indegree[j] += 1
            path.pop()
            vis[i] = False
    if len(path) == len(graph):
        sequences.append(path.copy())


def dna_gen(num_frags, num_clues):
    DIRS = ["l", "r"]
    og = [frag_gen(random.randint(5, 6)) for _ in range(num_frags)]
    og = [*set(og)]
    fragments = set()
    # Take k pair from og and add the directional detail to fragments
    for _ in range(num_clues):
        fi = random.randint(0, len(og)-1)
        fj = random.randint(0, len(og)-1)
        if fi < fj:
            tmp = (og[fi], og[fj], "l")
        elif fi > fj:
            tmp = (og[fi], og[fj], "r")
        else:
            continue
        fragments.add(tmp)
    return fragments, og


def frag_gen(k):
    BASES = ["a", "c", "g", "t"]
    return "".join(random.choice(BASES) for _ in range(k))


def usage():
    print("Usage: dna NUM_FRAGS PLOT_SCALE")
    exit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    num_frags = int(sys.argv[1])
    x = []
    y = []
    for i in range(int(num_frags/2)*num_frags, num_frags*num_frags):
        fragments, og = dna_gen(num_frags, i)
        g = uu_graph()
        g.graph_construct(fragments)
        tmp = topo(g)
        print(i, len(tmp))
        x.append(i)
        y.append(len(tmp))
    plt.scatter(x, y, label=f"#(fragments) = {num_frags}")
    plt.yscale(sys.argv[2])
    plt.xlabel("Number of clues")
    plt.ylabel("Number of possible sequences(log)")
    plt.legend()
    plt.show()
