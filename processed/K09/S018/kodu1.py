from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend,täisarv):
    silutud = []
    n_viimast = []
    for i in range(len(järjend)):
        if len(n_viimast) < täisarv:
            n_viimast.append(järjend[i])
        else:
            n_viimast.append(järjend[i])
            n_viimast.pop(0)
        silutud.append(harmonic_mean(n_viimast))
    return silutud

faili_nimi = input("Sisesta faili nimi: ")
n = int(input("Sisesta n: "))

arvud = []
kuupäevad = []

with open(faili_nimi, "r", encoding="UTF-8") as f:
    järjend = f.read().replace("\n", ", ").split(", ")
    for i in range(0,len(järjend),2):
        kuupäevad.append(järjend[i])
        arvud.append(float(järjend[i+1]))
        
silutud = silu_andmed(arvud, n)

fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.plot(kuupäevad, arvud, label="Aktsia hind")
ax.plot(kuupäevad, silutud, label="Aktsia hind silutult")

ax.set_xlabel("Kuupäevad")
ax.set_ylim(0, 0.03)
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
ax.legend()

plt.show()