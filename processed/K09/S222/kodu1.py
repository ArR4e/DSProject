from statistics import harmonic_mean
import matplotlib.pyplot as joonis

def silu_andmed(l,n):
    uus_l = []
    o = 1
    while o < n:
        if o == 1:
            uus_l.append(harmonic_mean([l[0]]))
        else:
            uus_l.append(harmonic_mean(l[0:o]))
        o += 1
    for m in range(len(l)):
        if m+n <= len(l):
            uus_l.append(harmonic_mean(l[m:n+m]))
    return uus_l

fail = open("aktsiad.txt")
aktsiad = []
pikkused = []
pikkus = 0
for rida in fail:
    eraldatud = rida.strip().split(", ")
    aktsiad.append(float(eraldatud[1]))
    pikkus += 1
    pikkused.append(pikkus)
fail.close()

keskmine = silu_andmed(aktsiad,50)
joonis.plot(pikkused,aktsiad)
joonis.plot(pikkused,keskmine)

joonis.show()
