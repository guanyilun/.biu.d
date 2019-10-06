import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def show(recipe, col):
    lines = sys.stdin.readlines()
    data = []
    col = int(col)
    for l in lines:
        fields = l.rstrip().split()
        try:
            float(fields[col])
        except:
            continue
        data.append(fields[col])
    plt.plot(data)
    plt.show()

def show2d(recipe):
    data_str = [l.rstrip().split() for l in sys.stdin.readlines()]
    print(data_str)
    data = []
    for vs in data_str:
        try:
            float(vs[0])
        except:
            continue
        data.append([float(v) for v in vs])
    data = np.array(data)
    print(data)
    plt.plot(data)
    plt.show()

def hist(recipe, col):
    lines = sys.stdin.readlines()
    data = []
    col = int(col)
    for l in lines:
        fields = l.rstrip().split()
        try:
            float(fields[col])
        except:
            continue
        data.append(fields[col])
    plt.hist(data, bins=50)
    plt.show()
