from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    vastus =[]
    pikkus = len(järjend)
    i=0
    if pikkus < n:
        n = pikkus
    while i<n:
        vastus.append(harmonic_mean(järjend[:i+1]))
        i +=1
    i = 0
    while pikkus > i+n:
        vastus.append(harmonic_mean(järjend[1+i: i+n+1]))
        i+=1
    return vastus
fail = input('Sisestage algandmete fail: ')
f = open(fail, encoding='UTF-8')
andmed = []
päevad = []
i = 0
for rida in f:
    päevad.append(1+i)
    rida = rida.split(', ')
    andmed.append(float(rida[1]))
    i +=1
f.close()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(päevad, andmed)
ax.plot(päevad, silu_andmed(andmed, 50))
plt.show()
