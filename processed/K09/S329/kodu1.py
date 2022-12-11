# 1. Andmete silumine

from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(ahk, n):
    kau = []
    m = []
    järjend = ahk[:]
    for i in ahk:
        m.append(järjend.pop(0))
        if len(m) > n:
            m.pop(0)
        keskmistatud = harmonic_mean(m)
        kau.append(keskmistatud)
    return kau


andmed = []
aeg = []
päevad = []

m = input("Sisestage faili nimi: ")
f = open(m, "r")
for rida in f:
    a = rida.strip('\n').split(', ')
    andmed.append(float(a[1]))
    aeg.append(a[0])
n = 50

f.close()

sissetulekud = andmed

kau = silu_andmed(andmed, n)
väljaminekud = kau

päevad = [i for i in range(1, len(aeg) + 1)]

fig = plt.figure()
ax = fig.add_subplot(1,1, 1)
ax.plot(päevad, sissetulekud)
ax.plot(päevad, väljaminekud)
ax.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
ax.set_xlim(1, len(aeg) + 50)
plt.show()


