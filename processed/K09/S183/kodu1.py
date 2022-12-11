from statistics import harmonic_mean
import matplotlib.pyplot as plt

# Arvutan harmoonilise keskmise
with open("aktsiad.txt", "r") as harmooniline:
    number = []
    for i in harmooniline:
        akt = i.strip("\n")
        akt2 = akt.split(", ")
        number += [float(akt2[1])]
    keskmine = harmonic_mean(number)


# Keskmiste uus järjend
def silu_andmed(järjend, n):
    kokku = []
    järg = 0
    k = 0
    for i in järjend:
        järg += 1
        mitmes = järg
        k += 1/i
        if järg > n:
            kordus = n
            k = 0
            while kordus != 0:
                k += 1/järjend[mitmes-kordus]
                kordus -= 1
            mitmes = n
        kokku += [mitmes/k]
    return kokku

with open("aktsiad.txt", "r") as aktsia:
    rida = len(aktsia.readlines())
    arv = silu_andmed(number, 50)


# Graafik
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(range(rida), number)
ax.plot(range(rida), arv)
ax.set_yticks([0, 0.0025, 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175]) # y-telg
ax.set_xticks([0, 200, 400, 600, 800, 1000]) # x-telg
plt.show() 
