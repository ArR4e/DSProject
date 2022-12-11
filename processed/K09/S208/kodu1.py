from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(jrj, arv):
    a = len(jrj)
    uus = []
    for i in range(len(jrj)):
        if (a-arv) > 0:
            uus.insert(0, harmonic_mean(jrj[(a-arv):a]))
        else:
            uus.insert(0, harmonic_mean(jrj[0:a]))
        a -= 1
    return uus

f = open(input("Sisesta faili nimi: "))
jrj, kuupäev = [], []
arv = 1
for rida in f:
    m = rida.strip().split(", ")
    jrj.append(float(m[1]))
    kuupäev.append(m[0])
hind = silu_andmed(jrj, arv)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(kuupäev, hind)
ax.set_xlabel("Päev")
ax.set_ylim(0, (max(jrj) + max(jrj)*0.1))
ax.set_xticks(kuupäev)
plt.show()
f.close()