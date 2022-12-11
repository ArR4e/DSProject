from statistics import harmonic_mean
import matplotlib.pyplot as plt

f = open("aktsiad.txt", encoding="UTF-8")

andmed = []   
for rida in f:
    osad = rida.split()
    andmed.append(osad[3])

def silu_andmed(x, y):
    vastus = []
    loplik = []
    
    for i in range(len(x)):
        if y > i:
            for andmed in range(i + 1):
                vastus.append(x[andmed])
            loplik.append(harmonic_mean(vastus))
            vastus.clear()
        else:
            for andmed2 in range(y):
                vahe = (i - andmed2)
                vastus.append(x[vahe])
            loplik.append(harmonic_mean(vastus))
            vastus.clear()
            
    return loplik
    
    
fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

ax.plot(silu_andmed)  
ax.set_xlabel("Aktsiad")        

plt.show()

silu_andmed()