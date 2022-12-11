import matplotlib.pyplot as plt
from statistics import harmonic_mean

aktsiahinnad = []
fail = open("aktsiad.txt", encoding = "UTF-8")
for rida in fail:
    rida = rida.strip("\n")
    rida = rida.split(",")
    rida = rida[1]
    aktsiahinnad.append(float(rida))
fail.close()

def silu_andmed(algandmed, täisarv):
    silutud = []
    n = 0
    samm = 1
    while True:
        if samm > len(algandmed):
            break
        elif len(algandmed) >= täisarv:
            while True:
                if samm > len(algandmed):
                    break
                elif samm <= täisarv:
                    harmooniline_keskmine = harmonic_mean(algandmed[n:samm])
                    silutud.append(harmooniline_keskmine)
                    samm += 1
                elif samm > täisarv:
                    n += 1
                    harmooniline_keskmine = harmonic_mean(algandmed[n:samm])
                    silutud.append(harmooniline_keskmine)
                    samm += 1
        else:
            while True:
                if samm <= len(algandmed):
                    harmooniline_keskmine = harmonic_mean(algandmed[0:samm])
                    silutud.append(harmooniline_keskmine)
                    samm += 1
                else:
                    break
    return silutud

silutud = silu_andmed(aktsiahinnad, 50)

joonis = plt.figure()
joonestusala = joonis.add_subplot(1, 1, 1)
joonestusala.plot(aktsiahinnad)
joonestusala.plot(silutud)
plt.show()
