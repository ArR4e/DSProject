from statistics import harmonic_mean

import matplotlib.pyplot as plt

fail = input("Sisestage faili nimi: ")
f = open(fail, encoding = 'UTF-8')
numbrid = []
kuupäev = []

for rida in f:
    korrastatud = rida.strip().split(',')
    kuupäev.append(korrastatud[0])
    numbrid.append(float(korrastatud[1]))


def silu_andmed(järjend,täisarv):
    uus = []
    teine = []
    i = 0
    for el in järjend:
        if i < täisarv:
            teine.append(järjend[i])
            k = harmonic_mean(teine)
            uus.append(k)
            i += 1
        else:
            teine.append(järjend[i])
            teine.pop(0)
            k = harmonic_mean(teine)
            uus.append(k)
            i += 1 
            
    return uus

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(numbrid)
ax.plot(silu_andmed(numbrid,3),"tab:orange")

plt.show()



f.close()

