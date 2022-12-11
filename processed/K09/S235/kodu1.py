import matplotlib.pyplot as plt
from statistics import harmonic_mean
def silu_andmed(järjend, n):
    b = 1
    silutud = []
    for el in järjend:
        if järjend.index(el) < n:
            a = järjend[0:järjend.index(el) + 1]
            silutud.append(float(harmonic_mean(a)))
        elif järjend.index(el) >= n:
            a = järjend[b:järjend.index(el)+1]
            silutud.append(float(harmonic_mean(a)))
            b += 1
    return silutud

f = input("Sisestage fail: ")
f = open(f)
f = f.readlines()

järjend = []
n = 50
for rida in f:
    rida = rida.strip().split(",")
    järjend.append(float(rida[1]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(järjend)
ax.plot(silu_andmed(järjend, n))
plt.show()
    
    