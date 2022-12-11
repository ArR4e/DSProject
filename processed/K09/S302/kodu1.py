from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(alg, arv):
    uus = []
    k = 0
    for el in alg:
        if k < arv:
            lol = alg[:k+1]
        else:
            lol = alg[k-arv+1:k+1]
        sisu = harmonic_mean(lol)
        uus.append(sisu)
        k += 1
    return(uus)
pv = 50
f = open("aktsiad.txt", "r")
read = f.readlines()
f.close()
päev = []
akt = []
kk = 0
for el in read:
    xd = el.strip("\n").split(" ")
    päev.append(kk +1)
    akt.append(float(xd[-1]))
    kk+=1

uus = silu_andmed(akt, pv)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(päev, uus, "orange")
ax.set_xlabel("Päevad")
ax.plot(päev, akt)
ax.set_ylim(0, 0.0175)
plt.show()