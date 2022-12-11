from statistics import harmonic_mean
def silu_andmed(järjend, n):
    uus = []
    for indeks in range(1, len(järjend) + 1):
        algus = max(0,indeks - n)
        a = harmonic_mean(järjend[algus:indeks])
        uus += [a]
    return uus
f = open("aktsiad.txt")
aktsiad = []
for rida in f:
    rida = rida.split()
    aktsiad += [float(rida[3])]
aktsiad_s = silu_andmed(aktsiad, 50)

import matplotlib.pyplot as plt
algandmed = aktsiad
aktsiad1 = aktsiad_s

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)
ax.plot(aktsiad1, "-r")
ax.plot(algandmed, "-b")

plt.show()