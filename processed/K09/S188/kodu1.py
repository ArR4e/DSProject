from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed, n):
    keskmistatud = []
    for i in range(len(algandmed)):
        esimene_tegur = i - n + 1
        if esimene_tegur < 0:
            esimene_tegur = 0
        vahemik = algandmed[esimene_tegur:i+1]
        keskmistatud += [harmonic_mean(vahemik)]
    return keskmistatud

f = open(input("Sisesta algandmete failinimi: "))

hinnad = []
kuupäevad = []

for rida in f:
    rea_järjend = rida.strip().split(",")
    hinnad += [float(rea_järjend[1].strip())]

for i in range(len(hinnad)):
    kuupäevad += [i+1]

plt.plot(kuupäevad, hinnad)
plt.plot(kuupäevad, silu_andmed(hinnad, 50))
plt.show()

f.close()