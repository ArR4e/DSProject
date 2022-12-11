from statistics import harmonic_mean
from copy import *
import matplotlib.pyplot as plt

def silu_andmed(algandmed, kesk):
    silutud = copy(algandmed)
    for i in range(len(algandmed)):
        if i+1 < kesk:
            silutud[i] = float(harmonic_mean(algandmed[:i+1]))
        elif i+1 >= kesk:
            silutud[i] = float(harmonic_mean(algandmed[i-kesk+1:i+1]))
    return silutud

fail = input("mis fail? ")

algandmed = []
with open (fail,"r", encoding = 'UTF-8') as f:
    for rida in f:
        algandmed += [rida.strip().split(",")]

hind = []
for el in range(len(algandmed)):
    hind += [float(algandmed[el][1])]
    
silutud = silu_andmed(hind, 50)

plt.plot(hind)
plt.plot(silutud)
plt.show()  
