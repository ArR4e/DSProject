from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(andmed, n):
    silutud = []
    for i in range(1, len(andmed)+1):
        if i <= n:
            silutud.append(harmonic_mean(andmed[0:i]))
        else:
            silutud.append(harmonic_mean(andmed[i-n:i]))
    return silutud

f = open(input("Sisesta faili nimi: "))
aktsia_hinnad = []
for rida in f:
    aktsia_hinnad.append(float(rida.split(", ")[1].strip("\n")))
f.close()
uued_andmed = silu_andmed(aktsia_hinnad, int(input("Sisesta mitme elemendi kaupa keskmist rakendada: ")))
plt.plot(aktsia_hinnad)
plt.plot(uued_andmed)

plt.show()