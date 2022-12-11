from statistics import harmonic_mean
import matplotlib.pyplot as plt

algandmed=[]
p2evad=[]
p=0

f=open("aktsiad.txt", "r")
for rida in f:
    p+=1
    rida=rida.strip()
    rida=rida.split(",")
    algandmed.append(float(rida[1]))
    p2evad.append(p)

def silu_andmed(a,b):
    andmed=[]
    k=-1
    for ele in a:
        keskmine=[]
        k+=1
        if k<b:
            i=k
            j=0
        else:
            i=k
            j=k-b+1
        while i>=j:
                keskmine.append(a[i])
                i-=1
        andmed.append(harmonic_mean(keskmine))
    return(andmed)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

uuedandmed=silu_andmed(algandmed, 50)
ax.plot(p2evad,algandmed)
ax.plot(p2evad,uuedandmed)

plt.show()