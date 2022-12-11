import matplotlib.pyplot as plt
from statistics import harmonic_mean
aktsiahinnad = []
failinimi = input("Sisesta failinimi: ")
with open(failinimi) as fail:
    for rida in fail:
        rida = float((rida.strip().split(", ", 1)[1]))
        aktsiahinnad.append(rida)

def silu_andmed(järjend, n):
    hind = []
    mitmes_indeks = 0
    for element in järjend:
        indeks = mitmes_indeks + 1
        if indeks >= n:
            kolmik = järjend[indeks - n:indeks]
            mitmes_indeks += 1
        else:
            kolmik = järjend[:indeks]
            mitmes_indeks += 1
        hind.append(harmonic_mean(kolmik))
    return hind

keskmistamine = silu_andmed(aktsiahinnad, 50)
algandmed = aktsiahinnad

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(algandmed)
ax.plot(keskmistamine)
plt.show()