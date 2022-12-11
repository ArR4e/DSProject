from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed, n):
    keskmistatud = []
    muut1 = 1
    muut2 = 1
    for i in range(1,len(algandmed)+1):
        if i <= n:
            c = harmonic_mean(algandmed[0:muut1])
            keskmistatud.append(c)
            muut1 += 1
        else:
            c = harmonic_mean(algandmed[muut2:muut1])
            muut2 += 1
            muut1 += 1
            keskmistatud.append(c)

    return keskmistatud

f = open("aktsiad.txt")

rida = f.readline()
muutuja = 0
silutud = []
kuupaev = []
hind = []

for rida in f:

    rida2 = rida.strip().split(',')
    silutud += rida2
    
    kuupaev.append(muutuja+1)
    muutuja += 1

for i in silutud:
    
    if silutud.index(i) % 2 != 0:
        hind.append(float(i))
        
hind1 = silu_andmed(hind, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuupaev, hind)
ax.plot(kuupaev, hind1)
ax.set_xlabel("Päevad")
ax.set_ylim(0,0.0175)
ax.set_xticks([0, 200, 400, 600, 800, 1000])

plt.show()

f.close()