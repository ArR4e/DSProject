from statistics import harmonic_mean
import matplotlib.pyplot as plt
# kõige pealt loon faili ja listi
def esialgne_list(fail):
    f = open(fail)
    järjend_hindadest = []
    for rida in f:
        rida = rida.strip().split(",")
        hind = rida[-1]
        järjend_hindadest.append(hind)
    f.close()
    # tagastan järjendi ujukomaarvudes, selleks loon uue tühja järjendi kuhu hiljem lisada float elemendid
    uus_järjend = []
    for element in järjend_hindadest:
        uus_element = float(element)
        uus_järjend.append(uus_element)

    return uus_järjend

def silu_andmed(järjend, n):
    muudetud_andmed = []
    eelmised_n = []
    for element in järjend:
        if len(eelmised_n) == n:
            eelmised_n.pop(0)
        eelmised_n.append(element)
        muudetud_andmed.append(harmonic_mean(eelmised_n))
    return muudetud_andmed

failinimi = input("Sisesta algandmete failinimi: ")
täisarv = int(input("Sisesta täisarv: "))
(esialgne_list(failinimi))
a = silu_andmed(esialgne_list(failinimi), täisarv)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(a, "-", label="harmooniline keskmine")
ax.plot(esialgne_list(failinimi), "-", label="esialgsed andmed")
ax.set_title("Aktsiahinnad")
ax.legend()
plt.show()
