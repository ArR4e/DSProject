from statistics import *
import matplotlib.pyplot as plt

def silu_andmed(l,n):
    l_hmean = []
    l.reverse()
    for el in range(len(l)):
        l_hmean.append(harmonic_mean(l[el:el+n]))
    l_hmean.reverse()
    return l_hmean

silu_andmed([1,2,3,4,5,6],3)

fail = input("Sisestage faili nimi: ")

f = open(fail,"r")
data = f.readlines()

l_alg = []

for i in range(len(data)):
    l_alg.append(float(data[i].split(",")[1].strip()))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(l_alg)
ax.plot(silu_andmed(l_alg,50))
plt.show()


