from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = input("Sisesta faili nimi: ")

f = open(fail, encoding = "utf-8")
hinnad = []
päevad = []
p = 1
for rida in f:
    rida = rida.strip()
    hind = rida.split(" ")[-1]
    hind = float(hind)
    hinnad += [hind]
    päevad += [p]
    p += 1

f.close()

def silu_andmed(järjend, n):
    harm_mean = []
    for indeks, element in enumerate(järjend):
        lõpp_indeks = indeks + 1
        if indeks < n:
            algus_indeks = 0
        else:
            algus_indeks = indeks - (n-1)
        el = harmonic_mean(järjend[algus_indeks:lõpp_indeks])
        harm_mean += [el]
    return harm_mean

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(päevad, hinnad)
ax.plot(päevad, silu_andmed(hinnad, 50))
#ax.set_xlabel("Harmooniline keskmine")

plt.show()  



    