# Andmete silumine

from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(jrj, n):
    silutud = []  #Tulemus järjend
    keskmista = []  #Keskmistamis järjend
    for i in range(len(jrj)):
        if len(keskmista) < n:  #Lisab keskmistamis järjendisse elemente kuni jõuab n-ni
            keskmista.append(jrj[i])
        else:
            keskmista.pop(0)   #Lisab järgmise algjärjendi elemendi ning eemaldab esimese keskmista elemendi
            keskmista.append(jrj[i])
        silutud.append(round(harmonic_mean(keskmista), 6))
    return silutud

#Lisan failis olevad andmed listi
f = open("aktsiad.txt", encoding="UTF-8")
aktsiad = []
for rida in f:
    päev, hind = rida.strip().split(",")
    aktsiad.append(float(hind))
f.close()

#Teen 2 listi, mille saan graafikule kuvada
keskmistatud_aktsiad = silu_andmed(aktsiad, 50)
päevad = list(range(1, len(aktsiad)+1))

#Graafiku joonistamne
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, aktsiad)
ax.plot(päevad, keskmistatud_aktsiad)
ax.set_label("päevad")
plt.show()
