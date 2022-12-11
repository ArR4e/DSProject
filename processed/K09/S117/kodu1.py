#alustasin 23.10.2021 (22:30)
from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(jarjend, n):
    copy = jarjend[:]
    uus_list = []
    harmonic_list = []
    for i in range(len(jarjend)):
        el = copy.pop(0)
        uus_list.append(el)
        if len(uus_list) > n: #kontrollime, kas on vaja esimest elemndi popida või mitte
            uus_list.pop(0)
        harmonic = harmonic_mean(uus_list)
        harmonic_list.append(harmonic)
    return harmonic_list

algandmed = input('Sisestage faili nimi: ')
f = open(algandmed)
hinnad = []
paevad = []
paev = 0

while True:
    rida1 = f.readline()
    if rida1 == '':
        break
    rida2 = rida1.split(',')
    hind = float(rida2[1])
    hinnad.append(hind)
    paev += 1
    paevad.append(paev)

f.close()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hinnad)
ax.plot(silu_andmed(hinnad, 50))
plt.show()