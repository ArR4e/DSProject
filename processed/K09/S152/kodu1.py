from statistics import harmonic_mean
import matplotlib.pyplot as plot

def silu_andmed(järjend, n):
    andmed = []
    j2 = []
    for i in range(len(järjend)):
        j2.append(järjend[i])
        if len(j2) > n:
            j2.pop(0)
        andmed.append(harmonic_mean(j2))
    return andmed

kasutaja_sisend = input("sisestage faili nimi: ")       
fail = open(kasutaja_sisend, "r")

hinna_järjend = []
päevade_arv = []
päev = 0
for rida in fail:
    sisu = rida.strip().split(", ")
    hind = sisu[1]
    päev +=1
    päevade_arv.append(päev)
    hinna_järjend.append(float(hind))
    
silutud = silu_andmed(hinna_järjend, 50)
fail.close()

plot.plot(päevade_arv,hinna_järjend)        
plot.plot(päevade_arv, silutud)
plot.title("Aktsiad")
plot.xlabel("")
plot.ylabel("")
plot.show()

