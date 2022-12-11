from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(arvud, samm):
    mean = []
    for i in range(1, len(arvud) + 1):
        j1 = []
        if i - samm <= 0:
            j1 = arvud[:i]
        else:
            j1 = arvud[i - samm:i]
        mean.append(harmonic_mean(j1))
    return mean

f = open(input())
nrPaevi = []
andmed = []
i = 1
for line in f:
    andmed.append(float(line.strip().split(', ')[1]))
    nrPaevi.append(i)
    i += 1
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(nrPaevi, andmed)
ax.plot(nrPaevi, silu_andmed(andmed, 50))
plt.show()

