import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, elemendid):
    n_järjend = []
    uus_järjend = []
    keskmine = 0
    for el in järjend:
        el = float(el)
        if len(n_järjend) < elemendid:
            n_järjend.append(el)
            keskmine = harmonic_mean(n_järjend)
            uus_järjend.append(keskmine)        
        else:
            n_järjend.append(el)
            del n_järjend[0]
            keskmine = harmonic_mean(n_järjend)
            uus_järjend.append(keskmine)
    return uus_järjend
   
f = open("aktsiad.txt", encoding = "UTF-8")

k_järjend = []
for rida in f:
    a_järjend = (rida.strip().split(", "))
    k_järjend.append((a_järjend[1]))

uus = silu_andmed(k_järjend, 3)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(k_järjend, uus)
ax.set_xlabel("aktsia hind")

plt.show()

f.close()

