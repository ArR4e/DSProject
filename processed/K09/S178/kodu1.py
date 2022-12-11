
sisestatud_fail = input("Sisesta failinimi: ") 
f = open(sisestatud_fail)
kuupäevad = []
järjend = []
for rida in f:
    rea_osad = rida.split(", ") 
    kuupäevad1 = rea_osad[0]
    järjend1 = float(rea_osad[1].strip("\n"))
    kuupäevad = (kuupäevad + [kuupäevad1])
    järjend = (järjend + [järjend1])


from statistics import harmonic_mean
n = 50
def silu_andmed(järjend, n):
    k = 1
    silutud = []
    for i in järjend:
        if k <= n:
            uus = harmonic_mean(järjend[0:k])
            k += 1
            silutud = (silutud + [uus])
        else:
            uus = harmonic_mean(järjend[k-n:k])
            silutud = (silutud + [uus])
            k += 1
    return(silutud)

(silu_andmed(järjend, n))

import matplotlib.pyplot as plt

fig = plt.figure()          
ax = fig.add_subplot(1,1,1)

ax.plot(kuupäevad, järjend, "-", label="Algandmed")
ax.plot(kuupäevad, silu_andmed(järjend, n), "-r", label="Silutud")

ax.set_xlabel("Kuupäevad")
ax.set_ylim(0, max(järjend)+0.001) 
ax.set_xticks(kuupäevad)
ax.set_ylabel("Aktsia hind")
ax.legend()

plt.show() 