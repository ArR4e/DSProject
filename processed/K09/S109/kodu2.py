def silu_andmed(a, n):
    from statistics import harmonic_mean
    keskmine = harmonic_mean(a)
    return keskmine

sisend = input("Sisesta faili nimi: ")
f = open(sisend, encoding="UTF-8")
from statistics import harmonic_mean
import matplotlib.pyplot as plt
aktsiad = []
kuupäev = []

for rida in f:
    rida = rida.strip("\n")
    rida = rida.split(", ")
    if len(rida) == 2:
        päev = (rida[0])
        nimi = float(rida[1])
        aktsiad.append(nimi)
        kuupäev.append(päev)
        
print(aktsiad)
print(kuupäev)
keskmine = []
i = 0
while i <= 1024:
    k = (harmonic_mean(aktsiad))
    keskmine.append(k)
    i += 1
    
print(keskmine)

ak = [aktsiad]
kesk = [keskmine]

fig = plt.figure()           
ax = fig.add_subplot(1, 1, 1)  

ax.plot(kuupäev, aktsiad)
ax.plot(kuupäev, keskmine)

ax.set_ylim(0.0000, 0.0175)
ax.set_xticks([0, 200, 400, 600, 800, 1000])

plt.show()
    