import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(alg_andmed, z):
    kesk_andmed = []
    n = 1
    
    for i in range(0, len(alg_andmed)):
                
        kesk_andmed.append(harmonic_mean(alg_andmed[i-n+1:i+1]))
        
        if n < z:
            n += 1
            
    return kesk_andmed


kuupaevad = []
hinnad = []

nimi = input("Sisestage faili nimi: ")
f = open(nimi, "r")

i = 0
for rida in f:
    kuupaevad.append(i)
    i += 1
    hinnad.append(float(rida[13:21]))
    
f.close()

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)

ax.plot(kuupaevad, hinnad, "b")
ax.plot(kuupaevad, silu_andmed(hinnad, 50), "r")  
ax.set_xlabel("Kuupäevad")
ax.set_ylabel("Aktsiahinnad")

ax.set_ylim(0.0000, 0.019)
ax.set_xticks([0, 200, 400, 600, 800, 1000])  

plt.show() 