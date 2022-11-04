#!/usr/bin/env python3
import random
from collections import defaultdict
from collections import deque

class uu_graph:
    def __init__(self):
        self.map = defaultdict(lambda :{"left":[],"right":[]})
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

    def topo(self):
        indegree = dict()
        # Queue of vertices with indegree of 0
        ready = deque()
        order = list()
        for i in self:
            indegree[i] = len(self.map[i]["left"])
            if indegree[i] == 0:
                ready.append(i)
        while ready:
            tmp = ready.popleft()
            order.append(tmp)
            for i in self.map[tmp]["right"]:
                # Reducing the dependency as tmp is added to the order. So it's
                # neighbours are free to enter the order as well
                indegree[i] -= 1
                # If it doesn't have any other dependencies add to ready queue
                if indegree[i] == 0:
                    ready.append(i)
        return order


def dna_gen(k):
    DIRS = ["l","r"]
    og = [frag_gen(random.randint(1,2)) for _ in range(k)]
    og = [*set(og)]
    fragments = set()
    # Take k pair from og and add the directional detail to fragments
    for _ in range(2*k):
        fi = random.randint(0,len(og)-1)
        fj = random.randint(0,len(og)-1)
        if fi < fj:
            tmp = (og[fi],og[fj],"l")
        elif fi > fj:
            tmp = (og[fi],og[fj],"r")
        else:
            continue
        fragments.add(tmp)
    return fragments, og


def frag_gen(k):
    BASES = ["a","c","g","t"]
    return "".join(random.choice(BASES) for _ in range(k))

if __name__ == "__main__":
    fragments, og = dna_gen(10)
    for i in fragments:
        print(i)
    g = uu_graph()
    g.graph_construct(fragments)
    for i in g:
        print(i, g.map[i])
    print(f"Original sequence: {og}")
    print(g.topo())
