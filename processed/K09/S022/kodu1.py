from statistics import harmonic_mean
import matplotlib.pyplot as plt
import copy
#fail = open("aktsiad.txt", "r")
fail = open(input("Utle faili nimi: "))
#n = input("n")
hinnad = []

for hind in fail:
    rida2 = hind.split(" ")
    rida2[3] = rida2[3].strip()
    ohind = rida2[3]
    hinnad.append(float(ohind))

#hinnad = [2, 1, 3, 4, 5]
#n = 50

def silu_andmed(hinnad, n):
    hinnadalg = []
    hinnadalg = copy.deepcopy(hinnad)
    arv = 1
    uksslist = []
    a = []
    kp = []
    for hind in hinnad:
        a.append(hind)
        if arv > n:
            a.pop(0)
        b = harmonic_mean(a)
        uksslist.append(b)
        kp.append(arv)
        arv = arv + 1
    return uksslist
    #print(uksslist)
    #print(range(len(uksslist)))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kp,uksslist)
ax.plot(kp,hinnadalg)
ax.set_xlabel("kuupaevad")
plt.show()

silu_andmed(hinnad, n)

