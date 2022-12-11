from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, arv):
    uus = []
    for i in range(len(järjend)):
        tegur = i + 1 - arv
        if tegur < 0:
            tegur = 0
        uus.append(harmonic_mean(järjend[tegur:i+1]))
    return uus

fail = input("Sisesta faili nimi: ")
f = open(fail, encoding="utf-8")
algandmed = []
pikkus = []
i = 0
for rida in f:
    rida = rida.strip().split(",")
    algandmed.append(float(rida[1]))
    pikkus.append(i)
    i += 1
f.close()

uued_andmed = silu_andmed(algandmed, 50)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(pikkus, algandmed)
ax.plot(pikkus, uued_andmed)
ax.set_ylim(0, 0.0175)
ax.set_xlim(0, len(pikkus))

plt.show()
