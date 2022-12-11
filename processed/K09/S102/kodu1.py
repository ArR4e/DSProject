from statistics import harmonic_mean
import matplotlib.pyplot as pl

f=open(input('Mis on algandmetefaili nimi? '))
def silu_andmed(a, n):
    b=[]
    c=[]
    for el in a:
        b.append(el)
        if len(b)>n:
            b.pop(0)
        c.append(harmonic_mean(b))
    return c
a=f.readlines()
b=[]
for i in range(len(a)):
    b.append(float(a[i].split(',')[1].strip()))
    
fig, ax=pl.subplots()
ax.plot(range(1,len(b)+1), silu_andmed(b, 3))
pl.plot(range(1,len(b)+1), b)
pl.show()
