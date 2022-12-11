from statistics import harmonic_mean
import matplotlib.pyplot as plt


fail = input("Sisesta faili nimi: ")
f = open(fail, "r", encoding = "UTF-8")

hinnad = []
päevad = []
i = 0
for rida in f:
    järjend = rida.split(",")
    hinnad.append(float(järjend[1].strip()))
    i += 1
    päevad.append(i)

def silu_andmed(hinnad,täisarv):
    number = 0
    keskmistatud = []
    viimased50 = []
    for arv in hinnad:
        number += 1
        if number <= täisarv:
            viimased50.append(arv)
            keskmistatud.append(harmonic_mean(viimased50))
        
        elif number > täisarv:
            viimased50.pop(0)
            viimased50.append(arv)
            keskmistatud.append(harmonic_mean(viimased50))

    return keskmistatud

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(päevad,hinnad)
ax.plot(päevad,silu_andmed(hinnad,täisarv))

ax.set_xlabel("Päevad")

plt.show()
    
f.close()