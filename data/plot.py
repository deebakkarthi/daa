#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt

def usage():
    print("Usage: plot FILE")

def plot(df, key, label):
    basename = sys.argv[1].split(".")[0]
    filepath = f"plots/{basename}/{basename}_{key}.png"
    x = df['input_size']
    y = df[key]

    plt.figure(figsize=(20,20))
    plt.xlabel("Input Size", fontsize=20, fontname="monospace")
    plt.ylabel(label, fontsize=20, fontname="monospace")
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    plt.plot(x, y, color="green")
    plt.savefig(filepath)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(0)

    df = pd.read_csv(sys.argv[1])
    label = {"input_size":"Input Size",
             "comp":"Comparisons",
             "swap":"Swaps",
             "basic":"Basic Operations",
             "time":"Time (ns)",
             "mem":"Memory (B)"}
    for i in df.columns:
        plot(df, i, label[i])
