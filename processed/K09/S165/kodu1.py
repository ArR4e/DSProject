from statistics import harmonic_mean
from matplotlib import pyplot as plt


def silu_andmed(järjend, n):
    algne_pikkus = len(järjend)
    for i in range(len(järjend)):
         if i == 0:          
             järjend.append( harmonic_mean([järjend[i]]) )
             
         
         elif n > i + 1:
             järjend.append( harmonic_mean(järjend[0:i+1]) )
             
         else:
             järjend.append( harmonic_mean(järjend[i-(n-1):i+1]) )
    
    return järjend[(algne_pikkus):]



andmete_fail = input("Palun sisestage faili nimi: ")

f = open(andmete_fail)
järjend = f.readlines()

for i in range(len(järjend)):
    järjend[i] = float(järjend[i].split(",")[1].strip())


hinnad = järjend
päevad = list(range(len(järjend)))


plt.plot(päevad, hinnad)

keskmistatud_hinnad = silu_andmed(järjend,50)

plt.plot(päevad, keskmistatud_hinnad)

plt.show()



f.close()

    
    
    
    




      
   
   
   
   