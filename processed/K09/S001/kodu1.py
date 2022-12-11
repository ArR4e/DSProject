from statistics import harmonic_mean
from matplotlib import pyplot

def silu_andmed(aktsia,arv):
    kesk = []
    for n in range(len(aktsia)):
        if n >= arv:
            kesk.append(harmonic_mean(aktsia[n-arv+1:n+1]))
        else:
            kesk.append(harmonic_mean(aktsia[0:n+1]))
    return kesk

fail = open(input("Faili nimi: "))
arv = int(input("Mitu numbri harmooniline keskmine: "))
aktsia = []
for rida in fail:
    rida = rida.split(",")
    aktsia.append(float(rida[1].strip()))
fail.close()
kesk = silu_andmed(aktsia,arv)

x_telje = []
for n in range(len(aktsia)):
    x_telje.append(n+1)

fig = pyplot.figure()
graafik1 = fig.add_subplot(1,1,1)
graafik1.plot(x_telje,aktsia)
graafik1.plot(x_telje,kesk)
pyplot.show()