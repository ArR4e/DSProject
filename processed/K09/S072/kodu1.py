from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    result = []
    
    for i in range(1, len(järjend) + 1):
        if i < n:
            result.append(harmonic_mean(järjend[0:i]))
        else:
            result.append(harmonic_mean(järjend[i-n:i]))
            
    return result

sisend_f = input("Palun sisestage algandmete faili nimi: ")

with open(sisend_f, 'r') as f:
    algandmed = f.read().splitlines()
    algandmed = [float(x.split(', ')[1]) for x in algandmed]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot([x for x in range(len(algandmed))], algandmed, "b-", label="Algandmed")
ax.plot([x for x in range(len(algandmed))], silu_andmed(algandmed, 50), "r-", label="Silutud andmed")

plt.show()
