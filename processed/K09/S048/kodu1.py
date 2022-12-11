import matplotlib.pyplot as plt
from statistics import harmonic_mean

aktsiad = []
fail = open("aktsiad.txt", encoding = "UTF-8")
for i in fail:
    i = i.strip("\n")
    i = i.split(",")
    i = rida[1]
    aktsiad.append(float(i))
fail.close()

def silu_andmed(algandmed, täisarv):
    silutud = []
    a = 0
    b = 1
    while True:
        if b > len(algandmed):
            break
        elif len(algandmed) >= täisarv:
            while True:
                if b > len(algandmed):
                    break
                elif b <= täisarv:
                    harmooniline_keskmine = harmonic_mean(algandmed[a:b])
                    silutud.append(harmooniline_keskmine)
                    b += 1
                elif b > täisarv:
                    a += 1
                    harmooniline_keskmine = harmonic_mean(algandmed[a:b])
                    silutud.append(harmooniline_keskmine)
                    b += 1
        else:
            while True:
                if b <= len(algandmed):
                    harmooniline_keskmine = harmonic_mean(algandmed[0:b])
                    silutud.append(harmooniline_keskmine)
                    b += 1
                else:
                    break
    return silutud

silutud = silu_andmed(aktsiad, 50)

joonis = plt.figure()
joonestusala = joonis.add_subplot(1, 1, 1)
joonestusala.plot(aktsiad)
joonestusala.plot(silutud)
plt.show()