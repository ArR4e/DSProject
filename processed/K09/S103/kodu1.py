import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend,n):
    tulemus = []
    for i in range(1,len(järjend)+1):
        if i < n and i > 0:
            harmooniline_keskmine = harmonic_mean(järjend[0:i])
            tulemus.append(harmooniline_keskmine)
        else:
            harmooniline_keskmine = harmonic_mean(järjend[i-n:i])
            tulemus.append(harmooniline_keskmine)
    return tulemus


fail = open("aktsiad.txt", encoding="utf-8")
aktsia_hinnad = []
for rida in fail:
    j = rida.strip().split(",")
    aktsia_hind = float(j[1])
    aktsia_hinnad.append(aktsia_hind)
fail.close()

plt.plot(aktsia_hinnad)
plt.plot(silu_andmed(aktsia_hinnad,50))
plt.show()

