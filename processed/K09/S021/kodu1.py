from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi = str(input("Palun sisestage faili nimi: "))
n = int(input("Sisestage täisarvuline n väärtus: "))

f = open(nimi,"r", encoding = "UTF-8")

hinnajärjend = []
for rida in f:
    järjend = rida.strip().split()
    hind = [float(järjend.pop())]
    hinnajärjend += hind

def silu_andmed(järjend, täisarv):
    keskmistatudjärjend = []
    for indeks in range(1, len(järjend) + 1):
        algus = max(0, indeks - täisarv)
        h_keskmine = harmonic_mean(järjend[algus:indeks])
        keskmistatudjärjend += [h_keskmine]
    return keskmistatudjärjend

plt.plot(hinnajärjend)
plt.plot(silu_andmed(hinnajärjend, n))
plt.show()
