from statistics import harmonic_mean
f = open(input("Sisesta faili nimi:"))
read = f.readlines()
f.close()
def silu_andmed(jarjend, n):
    njarjend = []
    uus_jarjend = []
    for i in range(len(jarjend)):
        a = jarjend.pop(0)
        njarjend.append(a)
        if len(njarjend) > n:
            b = njarjend.pop(0)
        kesk = harmonic_mean(njarjend)
        uus_jarjend.append(kesk)
    return uus_jarjend
aktsiad = []
for aktsia in read:
    a = aktsia.rstrip()
    jaotus = a.split(", ")
    aktsiad.append(float(jaotus[1]))

import matplotlib.pyplot as plt

fig = plt.figure()      
ax = fig.add_subplot(1,1,1)  

ax.plot(list(range(1025)), aktsiad)
ax.plot(list(range(1025)), silu_andmed(aktsiad, 50))  

ax.set_ylim(0.0000, 0.0175)   
ax.set_xticks([0, 200, 400, 600, 800, 1000]) 

plt.show()  