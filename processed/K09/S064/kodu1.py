#1. andmete silumine

from statistics import harmonic_mean
#harmooniline keskmine
import matplotlib.pyplot as plt
#graafik
fail = open(input("Sisestage algandmete faili nimi: "))
#aktsiad.txt

hinnad = []

for rida in fail:
    poolitan = rida.split(",")
    kuupäev = poolitan[0]
    hind = poolitan [1]
    aktsia = hind.strip("\n")
    hinnad += [float(aktsia)]

def silu_andmed(järjend, n):
    keskmine = []
    for el in range(len(järjend)):
        if el < n:
            uus = harmonic_mean(järjend[:el + 1])
            keskmine += [uus]
        else:
            uus = harmonic_mean(järjend[el + 1 - n:el +1])
            keskmine += [uus]
    return keskmine

silu_andmed(hinnad, 50)

#graafik
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(hinnad, label = "algandmed")
ax.plot(silu_andmed(hinnad, 50), label = "silutud andmed")
ax.set_ylim(0, 0.02)
ax.legend()
plt.show()

fail.close()
    