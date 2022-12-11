from statistics import harmonic_mean
import matplotlib.pyplot as plt

with open("aktsiad.txt") as f:
    andmed = f.read().splitlines()
    f.close()

hinnad = []
kuud = []
for el in andmed:
    n = el.split(", ")
    hinnad.append(n[1])
    kuud.append(n[0])

hinnad = [float(n) for n in hinnad]

def silu_andmed(jrd, a):
    jrd = [float(n) for n in jrd]
    if a > 0:
        keskmine = []
        i = 0
        for el in jrd:
            if i - a < 0:
                keskmine2 = harmonic_mean(jrd[0 : i + 1])
                keskmine.append(float(keskmine2))
                i += 1
            else:
                keskmine2 = harmonic_mean(jrd[i - a + 1 : (i + 1)])
                keskmine.append(float(keskmine2))
                i += 1
        return keskmine
    else:
        return False
    
päevad = range(0, (len(kuud)))
plt.plot(päevad, hinnad)
plt.plot(päevad, silu_andmed(hinnad, 50))
plt.show()    