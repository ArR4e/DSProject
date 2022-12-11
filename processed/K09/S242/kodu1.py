from statistics import harmonic_mean
faili_nimi = input("Sisesta faili nimi: ")
fail = open(faili_nimi)
silumata_järjend = []
päevad = 0
päevad_kasvavalt = []
for rida in fail:
    rida = rida.strip().split(', ')
    rida = [(rida[0], rida[1])]
    for kuupäev, hind in rida:
        silumata_järjend.append(float(hind))
        päevad += 1
        päevad_kasvavalt.append(päevad)



def silu_andmed(järjend, täisarv):
    järjend_silumiseks = []
    silutud_järjend = []
    for el in järjend:
        el = float(el)
        järjend_silumiseks.append(el)
        if len(järjend_silumiseks) > täisarv:
            järjend_silumiseks.pop(0)
        silutud_järjend.append(harmonic_mean(järjend_silumiseks))
    return silutud_järjend


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad_kasvavalt, silumata_järjend)
ax.plot(päevad_kasvavalt, silu_andmed(silumata_järjend, 50))
ax.set_ylabel("Aktsia hind")
plt.show()

