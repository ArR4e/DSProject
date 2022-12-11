import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(andmed, n):
    andmed.reverse()
    silutud_andmed = []
    for i in range(len(andmed)-1, -1, -1):
        silutud_andmed.append(harmonic_mean(andmed[i:i+n]))
    return silutud_andmed

faili_nimi = input("fail: ")

f = open("aktsiad.txt", encoding="utf-8")

sisu = f.readlines()

f.close()

n = 50

andmed = [ float(rida.split(",")[1]) for rida in sisu ]
silutud_andmed = silu_andmed(andmed, n)

x = [*range(len(andmed))]

andmed.reverse()
plt.plot(x, andmed, "cornflowerblue", label="Andmed")
plt.plot(x, silutud_andmed, "orange", label="Silutud andmed")

plt.show()
