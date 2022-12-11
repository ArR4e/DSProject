from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    silutud_järjend = []
    elemendid = []
    
    if järjend == []:
        return []
    
    elif n > len(järjend):
        for el in järjend:
            elemendid.append(el)
            silutud_järjend.append(harmonic_mean(elemendid))
        return silutud_järjend
    else:
        for x in range(0, n):
            elemendid.append(järjend[x])
            silutud_järjend.append(harmonic_mean(elemendid))

        for y in range(n, len(järjend)):
            elemendid.remove(elemendid[0])
            elemendid.append(järjend[y])
            silutud_järjend.append(harmonic_mean(elemendid))
        return silutud_järjend


f = open("aktsiad.txt")
andmed_failist = []
for rida in f:
    rida.strip("\n")
    andmed_failist.append(rida.split(","))
f.close()

algandmed = []
päevad = []
p = 0
for i in range(len(andmed_failist)):
    algandmed.append(float(andmed_failist[i][1]))
    päevad.append(p)
    p += 1
    
silutud_andmed = silu_andmed(algandmed, 50)

#graafikule tuleb saada järjendid silutud_andmed ja algandmed

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(päevad, algandmed)
ax.plot(päevad, silutud_andmed)

plt.show()