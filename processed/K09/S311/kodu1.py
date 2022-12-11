import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(algand, n):
    uus = []
    for i in range(len(algand)):
        if (i+1) < n:
            uus.append(harmonic_mean(algand[:i+1]))
        elif (i+1) >= n:
            uus.append(harmonic_mean(algand[:n]))
            algand.pop(0)
    return uus

nimi = input("Sisestage faili nimi: ")
f = open(nimi, "r", encoding= "UTF-8")
andm = f.readlines()
f.close()

originaal = []


for rida in andm:
    rida = rida.split(", ")
    originaal.append(float(rida[1]))
pikkus = len(originaal)
x_telg = list(range(pikkus))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x_telg, originaal)
ax.plot(x_telg, silu_andmed(originaal,50), color="orange")
ax.set_xlabel("Aktsiad")

plt.show()