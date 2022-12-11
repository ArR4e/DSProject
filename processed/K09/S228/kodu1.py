import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, n):
    ring = 0
    uus_järjend = []
    for i in range(len(järjend)):
        if ring == 0:
            kasutatav_järjend = järjend[i:i+1]
            keskmistatud = harmonic_mean(kasutatav_järjend)
            uus_järjend.append(keskmistatud)
            ring += 1
        elif ring < n:
            kasutatav_järjend = järjend[i-ring:i+1]  
            keskmistatud = harmonic_mean(kasutatav_järjend)
            uus_järjend.append(keskmistatud)
            ring += 1
        else:
            kasutatav_järjend = järjend[i+1-n:i+1]
            keskmistatud = harmonic_mean(kasutatav_järjend)
            uus_järjend.append(keskmistatud)
    return uus_järjend

nimi = input('Sisesta faili nimi: ')
f = open(nimi, encoding = 'UTF-8')

#Faili andmete põhjal koostan järjendi
andmed = []
for rida in f:
    rida_ok = rida.strip().split(', ')
    andmed.append(rida_ok[-1])
f.close()

#Teisendan järjendi elemendid (sõne -> ujukomaarv)
andmed = list(map(float, andmed))
n = 50

keskmistatud_andmed = silu_andmed(andmed, n)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmed)
ax.plot(keskmistatud_andmed)
ax.set_ylabel("Aktsiate hind")

plt.show()