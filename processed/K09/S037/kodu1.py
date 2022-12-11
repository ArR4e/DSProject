from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = input("Sisestage faili nimi: ")
f=open(fail, 'r')
j = []
for rida in f:
    rida = rida.strip().split(", ")
    arv = rida[1]
    j += [arv]
    algandmed = [float(el) for el in j]

def silu_andmed(järjend, n):
    silutud = []
    e = 0
    for i in järjend:
        m = 0
        s = e
        arvuks = []
        while m < n and s >= 0 and e <= len(järjend):
            arvuks += [järjend[s]]
            s -= 1
            m += 1
        keskmine = float(harmonic_mean(arvuks))
        silutud += [keskmine]
        e += 1
    return silutud

x_väärtus1 = range(0,len(algandmed))
y_väärtus = silu_andmed(algandmed, 50)
fig = plt.figure()
#ax = fig.add_subplot(1,1,1)

plt.plot(x_väärtus1,algandmed)
plt.plot(x_väärtus1, y_väärtus)

plt.show()
