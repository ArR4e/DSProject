from statistics import harmonic_mean
import matplotlib.pyplot as plt

aktsiad_algandmed = []
# laadi algandmed failist
with open("aktsiad.txt", "r") as aktsiad:
    for rida in aktsiad:
        aktsiad_algandmed.append(float(rida.strip().split()[-1]))

# aktsiate silumise funktsioon
def silu_andmed(algandmed, n):
    silutud_andmed = []
    for i in range(len(algandmed)+1):
        if i > n:
            silutud_andmed.append(harmonic_mean(algandmed[i-n:i]))
        elif i == 0:
            continue
        else:
            silutud_andmed.append(harmonic_mean(algandmed[:i]))
    return silutud_andmed

# loo teljestik
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# lisa graafikud
ax.plot(range(len(aktsiad_algandmed)), aktsiad_algandmed)
ax.plot(range(len(aktsiad_algandmed)), silu_andmed(aktsiad_algandmed, 50))

# kuva tulemused
plt.show()