from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(hinnad, n):
    järjend = []
    silutud_hinnad = []
    for indeks in range(1, len(hinnad)+1):
        järjend = hinnad[:indeks]
        while len(järjend) > n:
            järjend = järjend[1:]
        silutud_hinnad.append(harmonic_mean(järjend))
    return silutud_hinnad
        
fail = open("aktsiad.txt", "r")

hinnad = []
for rida in fail.readlines():
    hinnad.append(float(rida.split(",")[-1]))
    
silutud_hinnad = silu_andmed(hinnad, 50)

plt.plot(hinnad)
plt.plot(silutud_hinnad)
plt.xlabel("aaa")

plt.show()
