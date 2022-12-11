from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = open(input("Sisestage failinimi:"))
järjend = []
for rida in fail:
    b = rida.split(",")
    hind = b[1]
    hinnad = float(hind)
    järjend.append(hinnad)
def silu_andmed(järjend, täisarv):
    suvajärjend = []
    tagastatavj = []
    for el in järjend:
        suvajärjend.append(el)
        keskmine = harmonic_mean(suvajärjend)
        tagastatavj.append(keskmine)
        if len(suvajärjend) == täisarv:
            suvajärjend.pop(0)
    return tagastatavj
silutud = silu_andmed(järjend, 50)
xtelg= []
for i in range(len(järjend)):
    xtelg.append(i)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xtelg, järjend)
ax.plot(xtelg, silutud)
plt.show()