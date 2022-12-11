import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend,täisarv):
    uus = []
    for i in range(len(järjend)):
        uus.append(harmonic_mean(järjend[max(0,i-täisarv+1):i+1]))
    return uus

fail = input("Sisesta faili nimi: ")
n = int(input("Sisesta n: "))

with open(fail) as f:
    sisu = f.read().replace("\n",",").split(",")
    vaja = list(map(float,sisu[1::2]))
    print(vaja)
    
plt.plot(vaja)
plt.plot(silu_andmed(vaja, n))
plt.show()

