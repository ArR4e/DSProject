from statistics import harmonic_mean
from matplotlib import pyplot as plt

def silu_andmed(jarjend, taisarv):
    andmed = []
    jarjend2 = []
    for i in range(len(jarjend)):
        jarjend2.append(jarjend[i])
        if len(jarjend2) > taisarv:
            jarjend2.pop(0)
        andmed.append(harmonic_mean(jarjend2))
    return andmed
    
failinimi = input('Sisestage algandmete faili nimi: ')
fail = open(failinimi)
f = list(fail)
a = [elem.strip().split(',') for elem in f]

s = 0
hind = []
kuupaev = []
for i in a:
    hind.append(a[s][1])
    s +=1


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hind)
ax.plot(andmed)
plt.show()

fail.close()