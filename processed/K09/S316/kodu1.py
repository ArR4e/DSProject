from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(järjend,arv):
    arvutatud_keskmistused = []
    lühem_järjend = [järjend[0]]
    for el in järjend[1:]:
        keskmistus = harmonic_mean(lühem_järjend)
        arvutatud_keskmistused.append(keskmistus)
        if len(lühem_järjend) <= arv:
            lühem_järjend.append(el)
        else:
            lühem_järjend.pop(0)
    return arvutatud_keskmistused

fail = open(input("Sisesta faili nimi: "))
arv = int(input("Sisesta täisarv: "))

hindade_järjend = []
kuupäev = []
for rida in fail:
    if rida == "":
        break
    else:
        rea_list = rida.split(",")
        hind = float(rea_list[1])
        päev = rea_list[0]
        hindade_järjend.append(hind)
        kuupäev.append(päev)


fail.close()

joonis = plt.figure()
teljed = joonis.add_subplot(1,1,1)
teljed.plot(kuupäev,hindade_järjend)
plt.show()