from statistics import harmonic_mean
import matplotlib.pyplot as plt

with open("aktsiad.txt") as fail:
    andmed = fail.read().splitlines()
    fail.close()

hinnad = []
kuud = []
for el in andmed:
    n = el.split(",")
    hinnad.append(n[1])
    kuud.append(n[0])
    
hinnad = [float(n) for n in hinnad]


def silu_andmed(algandmed_järjendina, täisarv):
    algandmed_järjendina = [float(n) for n in algandmed_järjendina]
    if täisarv > 0:
        keskmine = []
        i = 0
        for el in algandmed_järjendina:
            if i - täisarv < 0:
                keskmine2 = harmon_mean(jrd[0 : i + 1])
                keskmine.append(float(keskmine2))
                i += 1
            else:
                keskmine2 = harmonic_mean(algandmed_järjendina[i - täisarv + 1 : (i + 1)])
                keskmine.append(float(keskmine2))
                i += 1
        return keskmine
    else:
        return False

päevad = range(0, (len(kuud)))
plt.plot(päevad, hinnad)
plt.plot(päevad, silu_andmed(hinnad, 50))
plt.show()