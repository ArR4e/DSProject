from statistics import harmonic_mean
from matplotlib import pyplot

def silu_andmed(algandmed, arv):
    har_jr = []
    silutud = []
    for el in algandmed:
        har_jr.append(el)
        if len(har_jr) <= arv:
            silutud.append(harmonic_mean(har_jr))
        else:
            har_jr.remove(har_jr[0])
            silutud.append(harmonic_mean(har_jr))
    return silutud

f = input('Sisestage algandmete faili nimi: ')
fail = open(f, 'r', encoding = 'UTF-8')
andmed = []
for rida in fail:
    andmed.append(rida.strip('\n').split(','))
fail.close()

aktsia_hinnad = []
for el in andmed:
    aktsia_hinnad.append(float(el[1]))

#print(silu_andmed(andmed,2))

#algandmete harmooniline keskmine
algandmete_har = silu_andmed(aktsia_hinnad, 50)
#print(algandmete_har)

#graafiku kujutamine
figure = pyplot.figure()
a = figure.add_subplot(1,1,1)
a.plot(algandmete_har)
a.plot(silu_andmed(aktsia_hinnad,3))

pyplot.show()

