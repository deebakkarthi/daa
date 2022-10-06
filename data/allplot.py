#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams["lines.linewidth"] = 2

def plot(dfd, key, label):
    filename = f"plots/all_{key}.png"
    plt.xlabel("Input Size", fontsize=20, fontname="monospace")
    plt.ylabel(label+" in log", fontsize=20, fontname="monospace")
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
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
