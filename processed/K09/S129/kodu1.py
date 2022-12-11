# Andmete silumine
from statistics import harmonic_mean
import matplotlib.pyplot as plt


with open("aktsiad.txt") as f:
    andmed = [float(rida.strip().split(", ")[1]) for rida in f]


def silu_andmed(sisend, n):
    counter = 0
    viimased = []
    
    for el in sisend:
        viimased.append(el)
        
        sisend[counter] = harmonic_mean(viimased)
        
        if len(viimased) == n:
            viimased.pop(0)

        counter += 1
    return sisend

'''
test = [2, 6, 3, 1, 2, 6]
print(silu_andmed(test, 4))
'''

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.plot(andmed)
ax.plot(silu_andmed(andmed, 50))
plt.show()
