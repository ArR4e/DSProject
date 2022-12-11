from statistics import *
from matplotlib.pyplot import *


def silu_andmed(a, b):
    silutud = []
    for x in range(0, len(a)):
        c = a[max(0, x - b + 1): x + 1]
        silutud.append(harmonic_mean(c))
    return silutud


algandmed = []
fail = input()
with open(fail, "r") as f:
    for rida in f:
        reaElemendid = rida.strip().split()
        algandmed.append(float(reaElemendid[3]))

mitu = int(input())
päevad = list(range(1, len(algandmed)+1))
andmed = silu_andmed(algandmed, mitu)

fig = figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(päevad, algandmed)
ax.plot(päevad, andmed)

show()
