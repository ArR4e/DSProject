from statistics import harmonic_mean
import matplotlib.pyplot as plt                 

f=open("aktsiad.txt", encoding="UTF-8")
hinnad=[]
for rida in f.readlines():
    jupid=rida.split(",")
    hinnad.append(float(jupid[1]))
f.close()        
def silu_andmed(hinnad, n):
    silutud=[]
    for i in range(len(hinnad)):
        silutud.append(harmonic_mean(hinnad[max(i-n+1,0):i+1]))
    return silutud
silu_andmed(hinnad, n)

silutud=silu_andmed(hinnad, 50)
fig = plt.figure()           
ax = fig.add_subplot(1,1,1)
ax.plot(hinnad)
ax.plot(silutud)
ax.set_ylabel("hinnad")

plt.show()