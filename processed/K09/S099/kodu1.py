from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(jär, n):
    silutud = []
    for i in range(0, len(jär)):
        if i < n:
            silutud.append(harmonic_mean(jär[:i+1]))
        else:
            silutud.append(harmonic_mean(jär[(i-n+1):i+1]))
    return silutud
    
f = open(input("Sisesta failinimi: "))
n = int(input("Sisesta täisarv n: "))
väärtused = []
for rida in f:
    väärtused.append(float(rida.split(",")[1]))
silutud = silu_andmed(väärtused, n)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(väärtused)
ax.plot(silutud)
ax.set_ylabel("Aktsia hind €")

plt.show()
