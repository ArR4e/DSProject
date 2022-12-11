from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = open("aktsiad.txt", encoding="UTF-8")
ridu = 0
hinnad = []
keskmine = []
algne = []

def silu_andmed (hind, samm):

    while len (hind) >= samm:
        ajutine = hind [(len (hind) - samm) : (len (hind))]
        keskmine.append(harmonic_mean(ajutine))
        hind.pop()

    while len (hind) > 0:
        ajutine = hind [0 : (len (hind))]
        keskmine.append(harmonic_mean(ajutine))
        hind.pop()

    keskmine.reverse()
    return keskmine

for rida in fail:
    x = rida.split(",")
    hinnad.append (float(x[1].strip ("\n")))
    algne.append (float(x[1].strip ("\n")))
    ridu += 1

fail.close()

mitme_kaupa = int (input ("Mitme kaupa: "))

while ridu < mitme_kaupa:
    mitme_kaupa = int (input ("Hindu on " + str(ridu) + " päeva kohta. Mitme päeva kaupa soovid keskmist rakendada: "))


keskmised = silu_andmed (hinnad, mitme_kaupa)

fig = plt.figure()           
ax = fig.add_subplot(1,1,1)  

ax.plot(algne)               
ax.plot(keskmised)           

plt.show()


    
