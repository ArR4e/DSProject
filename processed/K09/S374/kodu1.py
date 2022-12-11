import matplotlib.pyplot as plt
import numpy as np

def silu_andmed(massiiv, n):
    uus_massiiv = []
    nimetaja = 0
    j=0
    taisarvud = []
    
    for i in range(1, n+1):
        taisarvud.append(i)
    
    for i in range(0, len(massiiv)):
        if i >= n:
            lugeja = taisarvud[n-1]
        else:
            lugeja = taisarvud[i]
            
        nimetaja += 1/massiiv[i]

        if i >= n:
            nimetaja -= 1/massiiv[j]
            j += 1
            
        
        uus_element = lugeja/nimetaja
        uus_massiiv.append(uus_element)
        
    return uus_massiiv
        


faili_nimi = input('Sisestage faili nimi: ')
fail = open(faili_nimi, encoding = 'UTF-8')
paevad = []
hinnad = []

i = 0
for rida in fail:
    rida = rida.split(',')
    paevad.append(i)
    hinnad.append(float(rida[1]))
    i += 1
    
silutud = silu_andmed(hinnad, 50)

plt.plot(paevad, hinnad)
plt.plot(paevad, silutud)
plt.show()