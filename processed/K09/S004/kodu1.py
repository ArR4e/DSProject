from statistics import harmonic_mean
import matplotlib.pyplot as plt
tekstifail=input("Sisesta failinimi: ")
with open(tekstifail,"r") as f:
    hinnad=f.read().splitlines()
    hinnad=[x.split(",")[1] for x in hinnad]
def silu_andmed(andmed,n):
    tulemus=[]
    for x in range(len(andmed)):
        clist=[]
        a=0
        while a<n and x-a>-1:
            clist.append(float(andmed[x-a]))
            a+=1
        tulemus.append(harmonic_mean(clist))
    return(tulemus)
fig=plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot([i for i in range(len(hinnad))],silu_andmed(hinnad,50))
ax.plot([i for i in range(len(hinnad))],[float(i) for i in hinnad])
plt.show()