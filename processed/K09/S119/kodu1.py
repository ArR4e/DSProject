from statistics import harmonic_mean
f = open(input("Sisesta faili nimi: "))
a = f.readlines()
e = []
for i in a:
    d = i.split("\n")
    d = i.split(", ")
    e = e + [float(d[1])]

f.close()

def silu_andmed(jarjend, n):
    maksjarjend = [] # список значений, из которых нужно посчитать среднее значение
    keskjarjend = [] # список средних значений
    for el in range(len(jarjend)):
        b = jarjend.pop(0)
        maksjarjend = maksjarjend + [b]
        if len(maksjarjend) > n:
            c = maksjarjend.pop(0)
        harmonic = harmonic_mean(maksjarjend)
        keskjarjend = keskjarjend + [harmonic]
    return keskjarjend

import matplotlib.pyplot as plt


fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

ax.plot(list(range(1025)), e)
ax.plot(list(range(1025)), silu_andmed(e, 50))

      

plt.show()                   
        
        
        
        
        
    
