from statistics import harmonic_mean as har
import matplotlib.pyplot as plt
sisend=input("Faili nimi")
f=open(sisend,"r")
sisu=f.readlines()
f.close()
suurused=[]
for a in range(len(sisu)):
    sisu[a]=sisu[a].strip("\n")
    sisu[a]=sisu[a].split(", ")
    suurused.append(float(sisu[a][1]))
def silu_andmed(sisu,arv):
    silutud=[]
    for a in range(len(sisu)):
        if a>=arv:
            silutud.append(har(sisu[a-(arv-1):a+1]))
        else:
            silutud.append(har(sisu[0:a+1]))
    return(silutud)
plt.plot(suurused)
plt.plot(silu_andmed(suurused,50))
plt.show()