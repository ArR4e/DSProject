from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(andmed, n):
    uus = []
    ajutine = []
    for i in range(len(andmed)):
        if i < n-1:
            for el in range(i+1):
                ajutine.append(andmed[el])
        else:
            for el in range(i-n+1,i+1):
                ajutine.append(andmed[el])
        uus.append(harmonic_mean(ajutine))
        ajutine = []
    return uus

fail = open("aktsiad.txt","r")
tekst = fail.readlines()
fail.close()
x = []

for i in range(len(tekst)):
    x.append(i+1)
    tekst[i] = float(tekst[i].split(",")[1])
    
tekst2 = silu_andmed(tekst, 50)

plt.plot(x,tekst,label="Algne")
plt.plot(x,tekst2,label="Silutud")
plt.legend()
plt.show()