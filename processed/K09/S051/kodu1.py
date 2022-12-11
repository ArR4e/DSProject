from urllib.request import urlopen
import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, n):
    uued_andmed = []
    for i in range(len(järjend)):
        if n >= i:
            uued_andmed.append(harmonic_mean(järjend[:i+1]))
        else:
            uued_andmed.append(harmonic_mean(järjend[i-n+1:i+1]))
    return uued_andmed

fail = open(input("Sisesta faili nimi: "))
tekst = fail.read()
fail.close()
andmed = []
indeksid = []

for rida in range(len(tekst)):
    andmed.append(float(tekst[rida].split(',')[1]))
    indeksid.append(rida)

silutud_andmed = silu_andmed(andmed, int(input("Sisesta n: ")))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(indeksid, andmed, "b")
ax.plot(indeksid, silutud_andmed, "r")

plt.show()