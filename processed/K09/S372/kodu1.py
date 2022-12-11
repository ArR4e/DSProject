from statistics import harmonic_mean
import matplotlib.pyplot as plt
with open("aktsiad.txt", encoding="UTF-8") as hind:
    a = []
    for el in hind:
        rida = el.strip().split(", ")
        aktsia_hind = float(rida[1])
        a.append(aktsia_hind)
        
def silu_andmed(järjend, n):
    kokku = []
    for el in range(1,len(järjend)+1):
        if el < n and el > 0:
            keskmine = harmonic_mean(järjend[0:el])
            kokku.append(keskmine)
        else:
            keskmine = harmonic_mean(järjend[el-n:el])
            kokku.append(keskmine)
    return kokku
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(silu_andmed(a, 50))
ax.plot(a)
ax.set_ylim(0, 0.018)

plt.show()   
