from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(arvud, n):
    silutud_arvud = []
    for el in range(len(arvud)):
        kohast = el - n + 1
        if kohast <= 0:
            uus_el = harmonic_mean(arvud[:el+1])
            silutud_arvud.append(uus_el)
        else:
            uus_el = harmonic_mean(arvud[kohast:el+1])
            silutud_arvud.append(uus_el)
    return silutud_arvud

f = open('aktsiad.txt', 'r', encoding='utf-8')
n = int(input("Sisesta n: "))
arvud = []
for rida in f:
    sisu = rida.strip().split(', ')
    arvud.append(float(sisu[-1]))

silu_andmed(arvud, n)
plt.plot(silu_andmed(arvud, n))
plt.plot(arvud)
plt.show()

f.close()   