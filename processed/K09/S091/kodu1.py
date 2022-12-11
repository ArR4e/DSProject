from statistics import harmonic_mean as h
import matplotlib.pyplot as plt
from numpy import *
import numpy

f = open('aktsiad.txt', 'r')
a = f.readlines()
hinnad = []
for rida in a:
    kuupaev, hind = rida.strip().split(', ')
    hinnad.append(float(hind))

def silu_andmed(hinnad,number):
    hinnad_silutud = []
    for indeks in range(len(hinnad)):
        uusJarjend = []
        if indeks < number:
            for i in range(indeks+1):
                uusJarjend.append(hinnad[i])
            nr = round(h(uusJarjend), 12)
            hinnad_silutud.append(nr)
        else:
            for i in range(number):
                uusJarjend.append(hinnad[indeks - i])
            nr = round(h(uusJarjend), 12)
            hinnad_silutud.append(nr)
    return hinnad_silutud


numbrid = [i for i in range(len(hinnad))]
hinnad_silutud = numpy.array(silu_andmed(hinnad,50))
numbrid = numpy.array(numbrid)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(numbrid, hinnad_silutud, color='r')
ax.plot(numbrid, hinnad, color='g')

plt.show()


