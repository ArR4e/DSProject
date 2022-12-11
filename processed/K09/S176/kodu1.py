from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    keskmistatud = []
    aktsia_väärtus = []
    for el in järjend: 
        aktsia_väärtus += [el]
        if len(aktsia_väärtus) <= n:
            harm_keskmine = harmonic_mean(aktsia_väärtus)
            keskmistatud += [harm_keskmine]
        else:
            aktsia_väärtus.pop(0)
            harm_keskmine = harmonic_mean(aktsia_väärtus)
            keskmistatud += [harm_keskmine]
    return keskmistatud

f = open("aktsiad.txt", encoding = 'UTF-8')
hinnad = []
päev = 0
päevad = []
for rida in f:
    andmed = rida.strip().split(",")
    hind = andmed[-1]
    hinnad += [float(hind)]
    päev += 1
    päevad += [päev]
plt.plot(päevad, hinnad, silu_andmed(hinnad, 50))

plt.show()

f.close()