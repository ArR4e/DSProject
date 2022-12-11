from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    järjend.reverse()
    silutud = []
    for i in range(len(järjend)-1, -1, -1):
        silutud.append(harmonic_mean(järjend[i:i+n]))
    return silutud

n = 3
kõik = []
with open ("aktsiad.txt") as f:
    for sisu in f:
        sisu = sisu.strip().split(", ")
        nr = float(sisu[1])
        kõik += [nr]

joonis = plt.figure()
ala = joonis.add_subplot(1,1,1)

ala.plot(silu_andmed(kõik, n))
plt.show()