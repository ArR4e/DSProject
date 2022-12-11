from statistics import harmonic_mean
import matplotlib.pyplot as plt

#def silu_andmed(stonks, i):
    

fail=open("aktsiad.txt")
i=0
kp=[]
stonks=[]
for rida in fail:
    rida=rida.split(", ")
    kp.append(rida[i])
    i+=1
    stonks.append(rida[i].strip())
    i=0

põhi=plt.figure()
ala=põhi.add_subplot(1,1,1)
ala.plot(kp,stonks)

plt.show()