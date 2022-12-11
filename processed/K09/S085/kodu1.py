from statistics import harmonic_mean
import matplotlib.pyplot as plt
import numpy as np
def silu_andmed(järjend, n):
    i = 1
    tulemus = []
    for el in järjend:
        while i <= n and i <= len(järjend):
            a = harmonic_mean(järjend[0:i])
            i += 1
            tulemus.append(a)
        while n < len(järjend):
            if n >= len(järjend):
                break
            järjend.pop(0)
            a = harmonic_mean(järjend[0:n])
            tulemus.append(a)
    return tulemus
    
failinimi = input("Sisestage failinimi:")
f = open(failinimi)
kuupäevad = []
aktsiahinnad = []
for rida in f:
    jupid = rida.strip().split(",")
    kuupäev = jupid[0]
    hind = float(jupid[1])
    kuupäevad.append(kuupäev)
    aktsiahinnad.append(hind)
x = []
x = np.array(aktsiahinnad)
f.close()
c = silu_andmed(aktsiahinnad, n)
n = range(0, len(kuupäevad))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(n, x)
ax.plot(n, c)

plt.show()




    
