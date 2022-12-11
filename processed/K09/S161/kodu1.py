import matplotlib.pyplot as plt
from statistics import harmonic_mean
f=open("aktsiad.txt", encoding="UTF-8")
aktsiad=[]
for rida in f:
    x=rida.strip().split(", ")
    aktsiad.append(float(x[1]))
f.close()
def silu_andmed(aktsiad):
    arvud=[]
    uuedaktsiad=[]
    for rida in range(len(aktsiad)):
        arvud.append(aktsiad[rida])
        uuedaktsiad.append(harmonic_mean(arvud))
uuedaktsiad=silu_andmed(aktsiad)
indeks=[]
for rida in aktsiad:
    indeks.append(aktsiad.index(rida))
plt.plot(indeks, uuedaktsiad)
plt.xlabel("")       
plt.show() 