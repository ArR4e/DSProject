from statistics import harmonic_mean as hm
import matplotlib.pyplot as plt
nimi=input("sisesta algandmete faili nimi:")

f=open(nimi)
hinnad=[]
n=0
aeg=[]
k=50
def silu_andmed(x,y):
    o=0
    i=1
    andmed=[]
    while True:
        if x==[]:
            return x
            break
        while i<y and i<len(x):
            p=hm(x[o:i])
            andmed.append(p)
            i+=1
        if i==len(x):
            if i-y<0:
                andmed.append(hm(x[0:i]))
                return(andmed)
            andmed.append(hm(x[(i-y):i]))
            return(andmed)
            break
        o=i-y
        p=hm(x[o:i])
        andmed.append(p)
        i+=1
for r in f:
    l=r.split(",")
    hind=float((l[1]).strip("\n"))
    hinnad.append(hind)
    aeg.append(n)
    n+=1
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(aeg,hinnad)
ax.plot(aeg,silu_andmed(hinnad,k))

ax.set_xlabel("Aeg")
plt.show()
