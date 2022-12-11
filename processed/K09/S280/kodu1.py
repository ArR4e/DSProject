# 1. Andmete silumine / RP
import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, arv):
    n = 1
    uus = []
    
    for el in järjend:
        vajalik = n - arv
        if n <= arv:
            uus.append(harmonic_mean(järjend[:n]))
        else:
            uus.append(harmonic_mean(järjend[vajalik:n]))
        n += 1
        
    return uus
            

päevad = []
hinnad = []

nimi = input("Sisesta andmeid sisaldava faili nimi: ")

fail = open(nimi, encoding="UTF-8")
for päeva, rida in enumerate(fail):
    päevad.append(päeva+1)
    uus = rida.strip().split(" ")
    hinnad.append(float(uus[-1]))
fail.close()

silutud = silu_andmed(hinnad, 50)

joonis = plt.figure("Aktsia andmed")
ala = joonis.add_subplot(1,1,1)
ala.plot(päevad,hinnad)
ala.plot(päevad, silutud)
ala.set_xlabel("Päevad")
ala.set_ylabel("Hind (€)")
plt.title("Aktsia")

plt.show()