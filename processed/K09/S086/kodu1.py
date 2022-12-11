#Andmete silumine
from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(andmed, n):
    silutav = []
    silutud = []
    for i in range(len(andmed)):
        if i + 1 > n:
            silutav.pop(0)
        silutav.append(andmed[i])
        silutud.append(harmonic_mean(silutav))
    return silutud

f = open(input("Palun sisestage faili nimi: "))
kuupäevad = []
hinnad = []
algandmed = f.readlines()
for element in algandmed:
    andmepunkt = element.strip().split(", ")
    kuupäevad.append(andmepunkt[0])
    hinnad.append(float(andmepunkt[1]))
    
plt.plot(kuupäevad, hinnad, label = "algandmed")
plt.plot(kuupäevad, silu_andmed(hinnad, 25), label = "silutud")
plt.legend()
plt.show()
 
