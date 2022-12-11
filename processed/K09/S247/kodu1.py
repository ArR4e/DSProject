def silu_andmed(järjend, n):
    from statistics import harmonic_mean
    keskmistatud = []
    indeks = 0
    for el in järjend:
        if indeks <= n-1:
            keskmistatud.append(float(harmonic_mean(järjend[0:indeks + 1])))
            indeks += 1
        else:
            keskmistatud.append(float(harmonic_mean(järjend[indeks + 1-n:indeks + 1])))
            indeks += 1
    return keskmistatud
        
print(silu_andmed([2, 1, 3, 4, 5], 3))

fail = open(input("Sisestage algandmete fail: "), "r")
uus_järjend = []
for rida in fail:
    rida = rida.split(", ")
    hinnad = rida[1]
    uus_järjend.append(float(hinnad))
print(silu_andmed(uus_järjend,50))

import matplotlib.pyplot as plt

andmed = uus_järjend
korras = silu_andmed(uus_järjend, 50)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(andmed)
ax.plot(korras)

plt.show()
fail.close()














    
    
    