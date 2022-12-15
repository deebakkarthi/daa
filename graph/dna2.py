#!/usr/bin/env python3
import random
from collections import defaultdict
import sys
import matplotlib.pyplot as plt
from collections import deque


class uu_graph:
    def __init__(self):
        self.map = defaultdict(lambda: {"left": [], "right": []})

    def __len__(self):
        return len(self.map)

    def graph_construct(self, edgelist):
        for i in edgelist:
            (u, v, d) = i
            if d == "l":
                self.map[v]["left"].append(u)
            else:
                self.map[u]["right"].append(v)

    def indegree(self, v):
        return len(self.map[v]["left"])
    
    def neighbours(self, v):
        return self.map[v]["right"]

    def __iter__(self):
        for i in self.map:
            yield i

def topo(g):
    indegree = dict()
    # Queue of vertices with indegree of 0
    ready = deque()
    order = list()
    for i in g:
        indegree[i] = g.indegree(i)
        if indegree[i] == 0:
            ready.append(i)
    while ready:
        tmp = ready.popleft()
        order.append(tmp)
        for i in g.neighbours(tmp):
            # Reducing the dependency as tmp is added to the order. So it's
            # neighbours are free to enter the order as well
            indegree[i] -= 1
            # If it doesn't have any other dependencies add to ready queue
            if indegree[i] == 0:
                ready.append(i)
    return order



def dna_gen(num_frags):
    DIRS = ["l", "r"]
    og = [frag_gen(random.randint(5, 6)) for _ in range(num_frags)]
    og = [*(og)]
    fragments = list()
    for k,v in enumerate(og):
        for i in range(0,k):
            fragments.append((og[i],v,"l"))
        for i in range(k+1, len(og)):
            fragments.append((v,og[i],"r"))
    return fragments, og


def frag_gen(k):
    BASES = ["a", "c", "g", "t"]
    return "".join(random.choice(BASES) for _ in range(k))


def usage():
    print("Usage: dna NUM_FRAGS")
    exit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    num_frags = int(sys.argv[1])
    fragments, og = dna_gen(num_frags)
    for i in fragments:
        print(i)
    g = uu_graph()
    g.graph_construct(fragments)
    print(topo(g))
    print(og)
