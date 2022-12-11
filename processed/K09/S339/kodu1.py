from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = input("Sisestage faili nimi: ")
f = open(fail, "r", encoding = "UTF-8")
järjend = []
failis = []
for rida in f:
    tulp = rida.split(",")
    for tulbad in tulp:
        failis.append(tulbad.strip("\n"))

x = 1
for el in failis:
    uusuus = float(failis[x])
    x = x+2
    if x <= len(failis):
        continue
    else:
        break
arv = []
x = 0
while x < len(järjend):
    arv.append(x)
    x = x+1

lopp = silu_andmed(järjend, täisarv)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(arv, lopp)
ax.plot(arv, järjend)
plt.show()


def silu_andmed(järjend, täisarv):
    lopp = []
    x = 0
    y = []
    while x < (täisarv - 1) and x < len(järjend):
        uus = järjend[x]
        y.append(uus)
        keskmine = harmonic_mean(y)
        lopp.append(keskmine)
        x = x+1
    
    if täisarv >= len(järjend):
        return lopp
    else:
        indeks = täisarv - 1
        z = 1
        while True:
            last = järjend[indeks]
            keskmine2 = []
            keskmine2.append(last)
            z = 1
            while z <= (täisarv - 1):
                indeks2 = ((indeks)-z)
                keskmine2.append(järjend[x])
                z = z+1
            indeks = indeks+1
            if indeks == ((len(järjend))):
                keskmine = harmonic_mean(keskmine2)
                lopp.append(keskmine)
                break
            else:
                keskmine = harmonic_mean(keskmine2)
                lopp.append(keskmine)
                continue
        return lopp
                
                    