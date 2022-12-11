from statistics import *
import matplotlib.pyplot as plt
import numpy as np

aktsiad = input("sisesta faili nimi:")
algandmed = open(aktsiad, encoding = 'UTF-8')
kuupäevad = []
algnumbrid = []
for i in algandmed:
    rida = i.split(',')
    kuupäev = str(rida[0])
    algnr = float(rida[-1].strip())
    kuupäevad.append(kuupäev)
    algnumbrid.append(algnr)
    if i == '':
        break

    
def silu_andmed(alg, keskmine):
    hinnad = []
    global HinnadK 
    HinnadK = []
    keskmistH = 0
    j = 0
    for i in alg: 
        rida = i.split(',')
        hind = float(rida[-1].strip())
        hinnad.append(hind)
        j += 1
        if i == '':
            keskmistH = harmonic_mean(Hinnad)
            HinnadK.append(keskmistH)
        if j % (keskmine + 1) == 0:
            keskmistH = harmonic_mean(hinnad)
            HinnadK.append(keskmistH)
            keskmistH =0
            j = 0
            hinnad = []
               
    return HinnadK
    
        
x = kuupäevad
y = silu_andmed(algandmed, 50)
y2 = algnumbrid

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(y, '-r')
ax.plot(y2, '-b')

ax.set_xticks([0, 250, 500, 750, 1000])
ax.set_ylim(0, 0.02)
plt.show()