import matplotlib.pyplot as plt
import math
f = open("aktsiad.txt", "r")
andmed = []
päevad = []
päev = 0


for rida in f:
    rida = rida.strip()
    kõik = rida.split(", ", 2)
    kuu = kõik[0]
    andm_väärtus = kõik[1]
    andmed.append(float(andm_väärtus))
    päev += 1
    päevad.append(päev)
    
def silu_andmed(info, n):
    buffer = n * [0]
    kogu =[]
    
    for i in info:
        jagaja = 0
        jagatav = 0
        buffer.remove(buffer[0])
        buffer.append(i)
        
        for j in buffer:
            if j != 0:
                jagaja += 1/float(j)
                jagatav += 1
        uus_väärtus = jagatav / jagaja
        kogu.append(uus_väärtus)
    return kogu

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, andmed, label="Silumata andmed")
ax.plot(päevad, silu_andmed(andmed, 50), label="Silutud andmed")
ax.set_xlabel("Aeg")
ax.set_ylim(0,0.02)
ax.set_yticks([0.0, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
ax.legend()
plt.show()