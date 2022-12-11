import matplotlib.pyplot as plt
from statistics import harmonic_mean
f = open("aktsiad.txt")
read = f.readlines()
hinnad = []
for rida in read:
    aktsiad = rida.strip().split(", ")
    hinnad.append(float(aktsiad[1])) #lisab aktsiahinnad hindade järjendisse
print(hinnad) #prindib aktsiahindade järjendi
f.close()

def silu_andmed(algandmed, n):
    tulemused = [] 
    n_elementi = [] 
    for el in algandmed:
        n_elementi.append(el) #lisab järjendisse elemente vastavalt sellele palju neid oli algandmetes. 
        if len(n_elementi) > n:
            del(n_elementi[0])  #kustutab esimese elemendi kui järjendis on rohkem kui n elementi. 
        tulemused.append(float(harmonic_mean(n_elementi))) #lisab tulemused järjendisse 
    return tulemused

silutud = silu_andmed(hinnad, 50)

plt.plot(hinnad, label = "algandmed")
plt.plot(silutud, label = "silutud")
plt.legend()
plt.show()# Kuvame joonise ekraanile.

 
 
    
    
    