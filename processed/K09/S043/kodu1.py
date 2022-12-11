from statistics import harmonic_mean
import matplotlib.pyplot as plt
with open("aktsiad.txt") as f:
    jada1 = f.read().splitlines()
    f.close()

jada_ainthinnad = []
kuud = []
for el in jada1:
    x = el.split(', ')
    jada_ainthinnad.append(x[1])
    kuud.append(x[0])
    
jada_ainthinnad = [float(x) for x in jada_ainthinnad]
    

def silu_andmed(sisend, b):
    sisend = [float(x) for x in sisend]
    if b>0:
        harmoonia = []
        i = 0
        for el in sisend:
            if i-b<0:
                harmomaan = harmonic_mean(sisend[0:i+1])
                harmoonia.append(float(harmomaan))
                i = i+1
            else:
                harmomaan = harmonic_mean(sisend[i-b+1:i+1])
                harmoonia.append(float(harmomaan))
                i = i+1
        return harmoonia
            
    else:
        return False
    
##print(sillu_andmed(jada_ainthinnad, 3))


paevad = range(0, (len(kuud)))
plt.plot(paevad, jada_ainthinnad)
plt.plot(paevad, silu_andmed(jada_ainthinnad, 50))
plt.show()