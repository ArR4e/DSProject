import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(arvud, n):
    narvud = []
    hkeskmised = []
    for arv in arvud:
        if len(narvud) == n:
            narvud.pop(0)
            narvud.append(arv)
        else:
            narvud.append(arv)
        hkeskmised.append(harmonic_mean(narvud))
    return hkeskmised

andmed = []
fail = input("Sisesta fail: ")
narv = int(input("Sisesta n arv: "))

with open(fail) as f:
    for line in f.readlines():
        sisu = line.strip().split(",")
        andmed.append(float(sisu[1]))
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmed)
ax.plot(silu_andmed(andmed,narv))
plt.show()
