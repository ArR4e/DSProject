import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(jarjend, kaupa):
    uus_jarjend = []
    for i in range(len(jarjend)):
        if i < kaupa:
            uus_jarjend.append(harmonic_mean(jarjend[j] for j in range(i+1)))
        else:
            uus_jarjend.append(harmonic_mean(jarjend[j] for j in range(i-kaupa+1, i+1)))
    return uus_jarjend

f = open(input("Sisesta algandmete faili nimi: "), "r+", encoding="UTF-8")
mitmekaupa = int(input("Sisesta mitme kaupa: "))

paevad = 0
hinnad = []

for rida in f:
    paevad += 1
    hinnad.append(float((rida.strip("\n").split(", "))[-1]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(range(paevad), hinnad, "b", label="Algsed hinnad")
ax.plot(range(paevad), silu_andmed(hinnad, mitmekaupa), "r", label="Silutatud hinnad")
ax.set_xlabel("Päeva number")
ax.set_ylabel("Aktsia hind")
plt.show()

f.close()