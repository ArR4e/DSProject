from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    andmed = []
    keskmine = []
    n2 = n
    i = 0
    for el in järjend:
        andmed += [järjend[i]]
        keskmine += [harmonic_mean(andmed)]
        i += 1
        if len(andmed) > n:
            andmed.pop(0)
        try:
            järjend[i]
        except:
            return keskmine

fail = input('Sisestage faili nimi: ')
f = open(fail)
hinnad = [float((rida.split(',')[1]).strip()) for rida in f]
n1 = range(len(hinnad))

harm_keskmine = silu_andmed(hinnad, 50)

graafik = plt.figure()
ala = graafik.add_subplot(1,1,1)
ala.plot(n1, hinnad)
ala.plot(n1, harm_keskmine)

plt.show()

