from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(järjend, k):
    uus = []
    for indeks in range(1, len(järjend) + 1):
        if indeks < k and indeks > 0:
            harmooniline = harmonic_mean(järjend[0:indeks])
            uus.append(harmooniline)
        else:
            harmooniline = harmonic_mean(järjend[indeks-k:indeks])
            uus.append(harmooniline)
    return uus
        
fail = open("aktsiad.txt", encoding="utf-8")

hinnad = []
for rida in fail:
    päev = rida.strip().split(",")
    hind = float(päev[1])
    hinnad.append(hind)
fail.close()

plt.plot(hinnad)
plt.plot(silu_andmed(hinnad, 50))
plt.show()