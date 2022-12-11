from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(algne_jarjend, arv):
    tulemus = []
    n = 0
    for rida in algne_jarjend:
        if n < arv:
            x = algne_jarjend[:n + 1]
        else:
            x = algne_jarjend[n - arv + 1:n + 1]
        harmooniline_kesk = harmonic_mean(x)
        tulemus.append(harmooniline_kesk)
        n += 1
    return tulemus

fail = open("aktsiad.txt")
read = fail.readlines()
fail.close()
paev = []
aktsia = []
m = 0
l = 50
for rida in read:
    puhas = rida.strip().split(' ')
    paev.append(m + 1)
    aktsia.append(float(puhas[-1]))

uus_jarjend = silu_andmed(aktsia, l)

a = plt.figure()
b = a.add.subplot(1, 1, 1)

x.plot(paev, uus_jarjend, 'blue')
x.set_xlabel('paevad')
x.plot(paev, aktsia)
x.set_ylim(0, 0.0175)
plt.show()