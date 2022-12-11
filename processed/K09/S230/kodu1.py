import matplotlib.pyplot as plt
def silu_andmed(andmed,n):
    list=[]
    for i in range(len(andmed)):
        arv=float(0)  
        if i>=n:
            for a in range(n):
                arv+=(1/andmed[i-a])
            list+=[n/arv]
        else:
            for a in range(i+1):
                arv+=(1/andmed[i-a])
            list+=[(i+1)/arv]
    return list
        
fail=str(input("Sisestage faili nimi: "))
f=open(fail)
andmed=[]
päevad=[]
for i in f:
    i=i.strip().split(",")
    andmed+=[float(i[1])]
    päevad+=[i[0]]
silutud=(silu_andmed(andmed,50))

fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(päevad, silutud)  # Lisame joonestusalale joondiagrammi
ax.plot(päevad, andmed)
ax.set_xlabel("Päevad")        # ja x-telje pealkirja
ax.set_ylabel("Hind")

ax.set_xticks([päevad[0],päevad[int(len(päevad)/5*1)],päevad[int(len(päevad)/5*2)],päevad[int(len(päevad)/5*3)],päevad[int(len(päevad)/5*4)],päevad[len(päevad)-1]])  # ja x-telje märgid

plt.show()