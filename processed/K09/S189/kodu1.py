from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    järjend_uus = []
    for i in range(len(järjend)):
        if i < n:
            järjend_uus.append(harmonic_mean(järjend[x] for x in range(i+1)))
        else:
            järjend_uus.append(harmonic_mean(järjend[x] for x in range(i-n+1,i+1)))
    return järjend_uus
    
fail = open(input("Algandmete faili nimi: "), encoding="utf-8")
mitu_n = int(input("Mitme kaupa arvutatakse: "))
#print(silu_andmed([2, 1, 3, 4, 5], 3))

päev = 0
hind = []

for rida in fail:
    päev += 1
    hind.append(float((rida.strip("\n").split(", "))[-1]))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(range(päev), hind, label="Algsed")
ax.plot(range(päev), silu_andmed(hind, mitu_n), label="Silutud")
ax.set_xlabel("Päev")
ax.set_ylabel("Aktsia väärtus")
plt.show()

fail.close()