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

def plot(dfd, key, label):
    filename = f"../res/plots/all_{key}.pgf"
    plt.xlabel("Input Size")
    plt.ylabel(label+" in log")
    plt.yscale("log")
    for k,v in dfd.items():
        x = v["input_size"]
        y = v[key]
        plt.plot(x, y, label=k)
    plt.legend()
    plt.savefig(filename)
    plt.clf()


if __name__ == "__main__":
    keys = ["comp","swap","basic","time","mem"]
    labels = ["COMPARISONS","SWAPS","BASIC OPERATIONS",
              "TIME", "MEMORY (B)"]
    ldict = dict(zip(keys,labels))
    dfd = {}
    dfd["quick"] = pd.read_csv("quicksort.csv")
    dfd["merge"] = pd.read_csv("mergesort.csv")
    dfd["heap"] = pd.read_csv("heapsort.csv")
    dfd["insert"] = pd.read_csv("insertionsort.csv")
    dfd["bucket"] = pd.read_csv("bucketsort.csv")
    for i in keys:
        plot(dfd, i, ldict[i])
