from statistics import harmonic_mean
from matplotlib.pyplot import *
n = input("Sisestage täisarv: ")
#esmalt saame aktsia hinnad teada
f = open("aktsiad.txt")
aktsiad = []
for rida in f:
    a = rida.strip().split()
    aktsiad.append(float(a[-1]))

def silu_andmed(aktsiad, n):
    suvaline = []
    keskmistatud = []
    for x in range (0, len(aktsiad)):
        suvaline.append(aktsiad[x])
        if len(suvaline) >= int(n):
            suvaline.pop(0)
        keskmistatud.append(harmonic_mean(suvaline))
    return(keskmistatud)

#https://progeopik.cs.ut.ee/matplotlib.html
päevad = list(range(0, len(aktsiad)))
fig = figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(päevad, silu_andmed(aktsiad, n))  # Lisame joonestusalale joondiagrammi
show()                   # Kuvame joonise ekraanile.


    
