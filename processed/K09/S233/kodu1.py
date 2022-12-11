from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, arv):
    kesk = []
    n=1
    for i in range(len(järjend)):
        kesk.append(harmonic_mean(järjend[i-n+1:i+1]))
        
        if n<arv:
            n += 1
    return kesk

kuupäevad = []
hinnad = []

fail = open(input("Sisestage faili nimi:"),"r")

i = 0
for rida in fail:
    kuupäevad.append(i)
    i+=1
    hinnad.append(float(rida[13:21]))
fail.close()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(kuupäevad,hinnad)
ax.plot(kuupäevad,silu_andmed(hinnad,50))
plt.show()