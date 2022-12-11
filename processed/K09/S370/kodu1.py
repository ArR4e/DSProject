import copy
import matplotlib.pyplot as plt
from statistics import harmonic_mean
def silu_andmed(j, n):
    if n==1:
        return(j)
    else:
        for a in reversed(range(len(j))):
            elemendid=[]
            k=0
            while a-k>=0 and k!=n:
                elemendid= [j[a-k]]+elemendid
                k+=1      
            j[a]=harmonic_mean(elemendid)
        return(j)

kordaja=int(input("Mitme elemendi kaudu arvutada harmoonilist keskmist?"))
f=open("aktsiad.txt", "r")
hinnad=[]
kuupäevad=[]
päev=1
for rida in f:
    a=rida.split(",")
    hinnad.append(float(a[1].strip()))
    kuupäevad.append(päev)
    päev+=1
hinnad_korrigeeritud=silu_andmed(copy.deepcopy(hinnad),kordaja)
f.close

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.plot(kuupäevad, hinnad, "-",label="Hinnad")
ax.plot(kuupäevad, hinnad_korrigeeritud, "-r" ,label="Silutud hinnad")

ax.set_xlabel("Päevad")

ax.set_ylim(0, 0.0175)
plt.legend()
plt.xlabel("Päevad")
plt.ylabel("Hinnad")
plt.show()