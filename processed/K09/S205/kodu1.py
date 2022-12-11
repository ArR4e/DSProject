import matplotlib.pyplot as plt
import math

def silu_andmed(a,n):
    b=[]
    
    for i in range(len(a)):
        summa = 0
        if i < n-1:
            count = i
            while count >= 0:
                summa += 1/a[count]
                count -= 1
                
            b.append((i+1)/summa)
            
        else:
            
            for kord in range(n):
                summa += 1/a[i-kord]
            b.append(n/summa)
    return b

hind = []

with open(input('Palun sisesta faili nimi: '), 'r') as f:
    for rida in f:
        hind.append(float(rida.strip('\n').split(', ')[1]))

silutud = silu_andmed(hind,50)
vahemik = list(range(len(hind)))

graafik = plt.figure()
ax = graafik.add_subplot(1,1,1)
ax.plot(vahemik,hind)
ax.plot(vahemik, silutud,'^-r')

ax.set_xlabel("Hind")
#ax.set_ylabel("Hinnavahemik")

plt.show()