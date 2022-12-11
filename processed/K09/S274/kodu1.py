from statistics import harmonic_mean
import matplotlib.pyplot as plt

andmed = input("Sisesta failinimi: ")

f = open(andmed)
kuupäevad = []
hinnad = []

for rida in f:
    rea_osad = rida.strip().split(",")
    kuupäev = rea_osad[0]
    hind = float(rea_osad[1])
    kuupäevad = kuupäevad + [kuupäev]
    hinnad = hinnad + [hind]

f.close()

def silu_andmed(hinnad, täisarv):
    alamjärjend = []
    harm_järjend = []
    for i in range(0,len(hinnad)):
        if i < täisarv:
            alamjärjend = hinnad[0:(täisarv - (täisarv - 1) + i)]
            harm_hind = harmonic_mean(alamjärjend)
            harm_järjend = harm_järjend + [harm_hind]
        else:
            alamjärjend = hinnad[i - täisarv:i + 1]
            harm_hind = harmonic_mean(alamjärjend)
            harm_järjend = harm_järjend + [harm_hind]
    return harm_järjend
plt.plot(hinnad)
plt.plot(silu_andmed(hinnad, 50))
plt.show()
