from statistics import harmonic_mean
import matplotlib.pyplot as plt

failinimi = input('failinimi: ')
f = open(failinimi, 'r', encoding='UTF-8')

def silu_andmed(jarjend, n):
    silutud_jarjend = []
    harmoniseeruv = []
    for i in range(len(jarjend)):
        if i >= n:
            harmoniseeruv.pop(0)
        harmoniseeruv += [jarjend[i]]
        silutud_jarjend += [harmonic_mean(harmoniseeruv)]
    return silutud_jarjend

hinnad = []
paevad = []
reanr = 0
for rida in f:
    hind = float(rida[13:23])
    hinnad += [hind]
    reanr += 1
    paevad += [reanr]
joonis = plt.figure()
joonestusala = joonis.add_subplot(1,1,1)
joonestusala.plot(paevad, hinnad)
silutud = silu_andmed(hinnad, 50)
joonestusala.plot(paevad, silutud)
plt.show()
f.close()   
    
    