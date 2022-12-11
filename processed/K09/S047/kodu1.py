from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed, kesk_tegur):
    keskmised = []
   
    for i in range(len(algandmed)):
    
        if i < kesk_tegur-1:
            a = harmonic_mean(algandmed[:i+1])
        else:
            a = harmonic_mean(algandmed[i-kesk_tegur+1:i+1])
        
        keskmised += [a]
    
    return keskmised
        
         
fail=input("Sisesta faili nimi: ")

f=open(fail, "r")
read=f.readlines()
f.close()

arvud = []
for rida in read:
    jupid = rida.split(", ")
    arvud += [float(jupid[1])]
    
elemendid = range(0,len(arvud))
k=(silu_andmed(arvud, 20))

plt.plot(elemendid,arvud)
plt.plot(elemendid, k)  
           
plt.show()