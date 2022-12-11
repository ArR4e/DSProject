from statistics import harmonic_mean
import matplotlib.pyplot as plt

f_nimi = input("Sisestage algandmete faili nimi: ")
f = open(f_nimi, "r", encoding = "UTF-8")
hinnad = []
for rida in f:
    jupid = rida.strip().split(", ")
    kpv = jupid[0]
    hind = jupid[1]
    hinnad += [float(hind)]
f.close()

def silu_andmed(järjend, n):
    järjend2 = []
    silutud = []
    for el in järjend:
        järjend2 += [el]
        if len(järjend2) > n:
            del järjend2[0]
        silutud += [harmonic_mean(järjend2)]
    return silutud

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(silu_andmed(hinnad, 50))
plt.show()