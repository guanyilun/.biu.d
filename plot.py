import numpy as np
import matplotlib.pyplot as plt
import sys

def show(recipe):
    data_str = [l.rstrip() for l in sys.stdin.readlines()]
    data = []
    for v in data_str:
        try:
            float(v)
        except:
            continue
        data.append(float(v))
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
