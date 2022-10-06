#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
    })


def usage():
    print("Usage: plot FILE1 FILE2")

def plot(dfd, key, label):
    tmp = "vs".join(dfd.keys())
    filepath = f"../res/plots/{tmp}_{key}.pgf"
    plt.xlabel("Input Size")
    plt.ylabel(label)
    plt.yscale("log")
    for k,v in dfd.items():
        x = v["input_size"]
        y = v[key]
        plt.plot(x, y, label=k)
    plt.legend()
    plt.savefig(filepath)
    plt.clf()

def basename(p):
    p = p.split("/")[-1]
    p = p.split(".")[0]
    return p

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        exit(0)
    dfd = {}
    dfd[basename(sys.argv[1])] = pd.read_csv(sys.argv[1])
    dfd[basename(sys.argv[2])] = pd.read_csv(sys.argv[2])
    label = {"input_size":"Input Size",
             "comp":"Comparisons",
             "swap":"Swaps",
             "basic":"Basic Operations",
             "time":"Time (ns)",
             "mem":"Memory (B)"}
    for k,v in label.items():
        plot(dfd, k, v)
