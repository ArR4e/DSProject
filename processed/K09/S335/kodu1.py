from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    keskmistatud = []
    arvud = []
    järjend = järjend[::-1]
    if järjend == []:
        return []
    while True:
        arvud = arvud + [järjend[0:n]]
        järjend.remove(järjend[0])
        if järjend == []:
            break
    for grupp in arvud:
        keskmistatud += [harmonic_mean(grupp)]
    keskmistatud.reverse()
    return keskmistatud

fail = input("Sisestage faili nimi: ")
f = open(fail)
andmed = []
i = 0
päevad = []
for rida in f:
    a = rida.split(",")
    a = float(a[1].strip())
    andmed += [a]
    i += 1
    päevad += [i]

algandmed = andmed
silutud_andmed = silu_andmed(andmed, 50)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(päevad, algandmed)
ax.plot(päevad, silutud_andmed)

plt.show()

