from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(jarjend, n):
    harmoonilised_keskmised = []
    alamlist = []
    for o in range(1, n+1):
        for a in range(1, o+1):
            alamlist += [1/jarjend[a-1]]
        harm_keskmine = o/sum(alamlist)
        alamlist = []
        harmoonilised_keskmised += [harm_keskmine]
    idx = n
    for el in jarjend[n:]:
        harmoonilised_keskmised += [harmonic_mean(jarjend[idx-(n-1):idx+1])]
        idx += 1
    return harmoonilised_keskmised

f = open(input("Algandmete faili nimi: "),"r",encoding = "UTF-8")
jarjend = []
nr = 1
nrid = []
for rida in f.readlines():
    jarjend += [float(rida.split(", ")[1])]
    nrid += [nr]
    nr += 1
print()



fig = plt.figure()
ax = fig. add_subplot(1, 1, 1)

ax.plot(nrid, jarjend)
ax.set_xlabel("alright alright alright")
ax.plot(silu_andmed(jarjend, 50))
plt.show()

f.close()