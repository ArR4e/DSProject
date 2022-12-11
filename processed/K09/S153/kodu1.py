from statistics import harmonic_mean
import matplotlib.pylot as plt

f = open("aktsiad.txt", "r")
aktsia_hinnad = []
sisu = f.readlines()
for el in sisu:
    puhas = el.strip("\n")
    kaheks = puhas.split(", ")
    aktsia_hind = kaheks[1]
    aktsia_hinnad.append(aktsia_hind)

a = [float(i) for i in aktsia_hinnad]

n = int(input("Sisesta mitmekaupa keskmistamist rakendatakse: "))

def silu_andmed(a, n):
    i = 0
    keskmiste_list = []
    n_elemendi_list = []
    while i <= len(a)-n:
        n_elemendi_list.append(a[i])
        keskmiste_list.append(harmonic_mean(n_elemendi_list))
        i += 1
        if len(n_elemendi_list) == n:
            n_elemendi_list.clear()
            i += n
    return keskmiste_list
silu_andmed(a, n)

alghinnad = aktsia_hinnad
silutud = keskmiste_list

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(alghinnad, "-", label = "alghinnad")
ax.plot(silutud, "-", label = "silutud hinnad")
ax2.plot(n)
ax.set_ylabel("aktsia hinnad ja silutud hinnad")
plt.show()


