import matplotlib.pyplot as plt

from statistics import harmonic_mean
def silu_andmed(järjend, n):
    silutud_järjend=[]
    elemendid=[]
    
    for x in range(0, n):
        elemendid.append(järjend[x])
        silutud_järjend.append(harmonic_mean(elemendid))
        
    for y in range(n, len(järjend)):
        elemendid.remove(elemendid[0])
        elemendid.append(järjend[y])
        silutud_järjend.append(harmonic_mean(elemendid))
    return silutud_järjend


fail=input("Sisestage faili nimi: ")
f=open(fail)
järjend_hind=[]
järjend_aeg=[]
for line in f.readlines():
    rida=line.strip()
    nimi_ja_aeg=rida.split(',')
    hind=float(nimi_ja_aeg[1])
    järjend_hind.append(hind)
    aeg=nimi_ja_aeg[0]
    järjend_aeg.append(aeg)
    
silutud_andmed=silu_andmed(järjend_hind, 50)

fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)

ax.plot(järjend_aeg, järjend_hind)
ax.plot(järjend_aeg, silutud_andmed)

plt.show()
