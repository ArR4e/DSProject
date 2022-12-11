from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    #järjekorra number
    b = 0
    #loop mis koostab järjendi arvudest millest võtan harmoonilise keskmise
    harmean = []
    j = n
    for arv in järjend:
        n = j-1
        a = []
        while n >= 0:
            if b-n >= 0:
                a.append(järjend[b-n])
                n -= 1
            if b-n < 0:
                n -= 1
                continue
        c = harmonic_mean(a)
        harmean.append(c)
        b += 1
    return harmean
    
#PÕHIPROGRAMM

failinimi = input("Mis failist tahate lugeda? ")
hinnad = []
hindade_arv = []
arv1 = 1

f = open(failinimi)
rida = f.readline()

while True:
    rida = f.readline()
    if len(rida.strip()) == 0:
        break
    rea_järjend = rida.split(" ")
    hind = rea_järjend[-1]
    hind = float(hind.strip())
    hinnad.append(hind)
    hindade_arv.append(arv1)
    arv1 += 1

silutud_hinnad = silu_andmed(hinnad, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#ax.set_ylim(0,20)
ax.set_xticks([200,400,600,800,1000])

ax.plot(hindade_arv, hinnad, label="hinnad")
ax.plot(hindade_arv, silutud_hinnad, label="silutud hinnad")

plt.show()