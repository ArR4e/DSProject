#1. andmete silumine
import statistics
import matplotlib.pyplot as plt

def loo_list(fail):
    f=open(fail)
    read=[]
    for line in f:
        rida=line.strip().split(",")
        hind=rida[-1]
        read.append(hind)
    f.close()
    return [float(i) for i in read] #muudab kõik listi elemendid float type'iks

def silu_andmed(järjend, n):
    vastus=[]
    eelmised_n=[]
    for el in järjend:
        if len(eelmised_n)==n:
            eelmised_n.pop(0)
        eelmised_n.append(el)
        vastus.append(statistics.harmonic_mean(eelmised_n))
        
    return vastus
    
failinimi=input("Sisesta faili nimi: ")
täisarv=int(input("Sisesta positiivne täisarv: "))
a=silu_andmed(loo_list(failinimi), täisarv)

#print(silu_andmed(loo_list("aktsiad.txt"), 3))
#print(silu_andmed([2, 1, 3, 4, 5], 3))

#graafiku koostamine:
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(a, "-")
ax.plot(loo_list(failinimi), "-")
plt.show()