from statistics import harmonic_mean

def silu_andmed(algandmed,n):
    hkandmed=[]
    k=0
    for i in range(len(algandmed)):
        if i>=n-1:
            hkandmed+=[harmonic_mean(algandmed[i-(n-1):i+1])]
        else:
            hkandmed+=[harmonic_mean(algandmed[i-k:i+1])]
            k+=1
    return hkandmed

fail=input("Faili nimi: ")
f=open(fail, encoding="UTF-8")
algandmed=[]
for rida in f:
    algandmed+=[float(rida.split()[3])]
f.close()
f=open(fail, encoding="UTF-8")
read=f.readlines()
numbrid=[]
x=0
for rida in read:
    numbrid+=[x]
    x+=1



import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(numbrid,algandmed,"-b",label="Algandmed")
ax.plot(numbrid,silu_andmed(algandmed,50),"-r",label="Silutud andmed")
ax.set_ylim(0,0.02)
plt.show()

f.close()