from statistics import harmonic_mean
import matplotlib.pyplot as plt

sisend = input("Sisesta faili nimi: ")
f = open(sisend, encoding = "UTF-8")

def silu_andmed(järjend, arv):
    keskmistatud = []
    for i in range(len(järjend)):
        if i < arv:
            keskmine = harmonic_mean(järjend[0:i+1])
        else:
            keskmine = harmonic_mean(järjend[(i+1-arv):(i+1)])
            
        keskmistatud.append(keskmine)
        
    return keskmistatud


        


read = f.readlines()
hinnad = []
for rida in read:
    rida = rida.strip().split(", ")
    hind = float(rida[1])
    hinnad.append(hind)
    

siledad = silu_andmed(hinnad, 50)

plt.plot(hinnad)
plt.plot(siledad)
plt.show()



    