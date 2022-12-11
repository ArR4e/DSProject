from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, täisarv):
    uus_järjend = []
    i = 1
    arv = 1
    for el in järjend:
        if arv < täisarv:
            lisa = harmonic_mean(järjend[0:i])
            arv += 1
        else:
            lisa = harmonic_mean(järjend[(i-täisarv):i])
        uus_järjend += [lisa]
        i += 1
    return uus_järjend

f = open(input("Sisesta faili nimi: "))
andmed = []
kuupäevad = []
i = 0

for rida in f:
    tekst = rida.split(",")
    andmed += [float(tekst[1].strip("\n"))]
    i += 1
    kuupäevad += [i]

f.close()
silutud_andmed = silu_andmed(andmed, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuupäevad, silutud_andmed, "-r", label="Silutud andmed")
ax.plot(kuupäevad, andmed, "-b", label="Andmed")
ax.set_ylim(0.0000, 0.0175)         
ax.set_xlim(0, 1000)
ax.legend()

plt.show()