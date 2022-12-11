import matplotlib.pyplot as plt
from statistics import harmonic_mean

aktsiad = []
f = open("aktsiad.txt", encoding = "UTF-8")
for i in f:
    i = i.strip("\n")
    i = i.split(",")
    i = rida[1]
    aktsiad.append(float(i))
f.close()

def silu_andmed(arv, täisarv):
    silutud = []
    n = 0
    m = 1
    while True:
        if m > len(arv):
            break
        elif len(arv) >= täisarv:
            while True:
                if m > len(arv):
                    break
                elif m <= täisarv:
                    harmooniline_keskmine = harmonic_mean(arv[n:m])
                    silutud.append(harmooniline_keskmine)
                    m += 1
                elif m > täisarv:
                    n += 1
                    harmooniline_keskmine = harmonic_mean(arv[n:m])
                    silutud.append(harmooniline_keskmine)
                    m += 1
        else:
            while True:
                if m <= len(arv):
                    harmooniline_keskmine = harmonic_mean(arv[0:m])
                    silutud.append(harmooniline_keskmine)
                    m += 1
                else:
                    break
    return silutud

silutud = silu_andmed(aktsiad, 50)

joonis = plt.figure()
joonestusala = joonis.add_subplot(1, 1, 1)
joonestusala.plot(aktsiad)
joonestusala.plot(silutud)
plt.show()
