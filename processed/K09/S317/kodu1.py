import matplotlib.pyplot as plt
from statistics import harmonic_mean
failinimi = input("Sisesta failinimi: ")
fail = open(failinimi + ".txt", "r")
a = []
b = 50
for rida in fail:
    rida = rida.strip()
    rida = rida.split(" ")
    element = float(rida[-1])
    a.append(element)
def silu_andmed(a, b):
    a = a
    andmed = []
    global keskmised
    keskmised = []
    global algus
    algus = []
    for i in a:
        while a.index(i)+1<=b and i not in andmed:
            andmed.append(i)
            summa = 0
            for el in andmed:
                summa += 1/el
            keskmine = (a.index(i)+1)/summa
            keskmised.append(keskmine)
            algus.append(i)
            break
        else:
            while a.index(i)+1>b or i in andmed:
                del andmed[0]
                andmed.append(i)
                summa = 0
                for el in andmed:
                    summa += 1/el
                keskmine = b/summa
                keskmised.append(keskmine)
                algus.append(i)
                break
    return keskmised 
fail.close()
uus = silu_andmed(a, b)
joonis = plt.figure()
ax = joonis.add_subplot(1, 1, 1)
ax.plot(algus)
ax.plot(uus)
ax.set_xlabel("Näe!")
plt.show() 