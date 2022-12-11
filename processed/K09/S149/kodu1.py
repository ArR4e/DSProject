import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, kicker):
    uus_jada = []
    [uus_jada.append(harmonic_mean(järjend[max(0, i - kicker + 1) : i + 1])) for i in range(len(järjend))]
    return uus_jada

fail = input("Sisesta faili: ")
n = int(input("Sisesta n: "))

with open(fail) as f:
    jada = list(map(float, f.read().replace("\n", ", ").split(", ")[1::2]))

plt.plot(jada)
plt.plot(silu_andmed(jada, n))
plt.show()