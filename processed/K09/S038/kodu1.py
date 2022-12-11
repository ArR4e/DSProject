from statistics import harmonic_mean
import numpy as np

nimi = str(input("Sisestage soovitud faili nimi: "))
fail = open(nimi,"r")
aktsiad = []
for line in fail:
    uus = line.split(",")
    hind = uus[1].strip("\n")
    aktsiad.append(float(hind))
fail.close()

test = [1.2,3.4,5.6,7.8]

def silu_andmed(a,n):
    silutud = []  
    for i in range(1,len(a)+1):
        new = harmonic_mean(a[max(i-n,0):i])
        silutud.append(new)
    return silutud

import matplotlib.pyplot as plt
loplikud = silu_andmed(aktsiad,50)

hinnad =(loplikud)
aktslopp =(aktsiad)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(aktslopp,label="Algsed aktsiahinnad")
ax.plot(hinnad,label="Keskmistatud aktsiahinnad")

ax.set_xlabel("Päevad")
ax.set_ylim(0,max(aktsiad))
ax.set_yticks([0,0.0025,0.005,0.0075,0.01,0.0125])
ax.legend()

plt.show()

print(test)
print(silu_andmed(test,2))



    

    

