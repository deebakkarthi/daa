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
    print("Usage: plot FILE")


def plot(df, key, label):
    basename = sys.argv[1].split("/")[-1]
    basename = basename.split(".")[0]
    filepath = f"../res/plots/{basename}/{basename}_{key}.pgf"
    x = df['input_size']
    y = df[key]
    plt.xlabel("Input Size")
    plt.ylabel(label)
    plt.plot(x, y)
    plt.savefig(filepath)
    plt.clf()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(0)

    df = pd.read_csv(sys.argv[1])
    label = {"input_size": "Input Size",
             "comp": "Comparisons",
             "swap": "Swaps",
             "basic": "Basic Operations",
             "time": "Time (ns)",
             "mem": "Memory (B)"}
    for i in df.columns:
        plot(df, i, label[i])
