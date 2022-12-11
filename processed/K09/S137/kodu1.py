import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend,arv):
    if järjend == []:
        return järjend
    i = 0
    keskmine = []
    while i < arv:
        if i +1 > len(järjend):
            return keskmine
        keskmine+=[harmonic_mean(järjend[0:i+1])]
        i+=1
    while i < len(järjend):
        keskmine += [harmonic_mean(järjend[i-arv+1:i+1])]
        i+=1
    return keskmine
allikas = input("Kus on aktsiad: ")
f = open(allikas)
n = 50
andmed = []
kõik_päevad = []
for rida in f:
    rida = rida.split(',')
    andmed += [float(rida[1])]
    kõik_päevad +=[rida[0]]
    päev = rida[0].split(' ')
    #x telje pulgad   
silutud = silu_andmed(andmed,n)
kuud = kõik_päevad

fig = plt.figure()
ax = fig.add_subplot(1,1,1)  

ax.plot(kuud, andmed, "-", label="Väärtus")
ax.plot(kuud, silutud, "-", label="Keskmine väärtus")
pikkusj= [int(len(andmed)/6),int(len(andmed)/3),int(len(andmed)/2),int(len(andmed)/6 * 4),int(len(andmed)/6 * 5),len(andmed)]

ax.set_xlabel("Kuud")
ax.set_ylim(0, 0.02)         # Määrame y-telje nähtavuspiirkonna
ax.set_xticks(pikkusj)  # ja x-telje märgid
ax.legend()

plt.show()                   # Kuvame joonise ekraanile.