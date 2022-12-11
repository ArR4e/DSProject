from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(ahk, n):
    kau = []
    m = []
    järjend = ahk[:]
    for i in ahk:
        m.append(järjend.pop(0))
        if len(m) > n:
            m.pop(0)
        kesk = harmonic_mean(m)
        kau.append(kesk)
    return kau
    
data = []
aeg = []
päev = []

nimi = input('Sisesta faili nimetus: ')
fail = open(nimi, 'r')
for r in fail:
    uus_r = r.strip('\n').split(', ')
    data.append(float(uus_r[1]))
    aeg.append(uus_r[0])
n = 50

fail.close()

sisse = data

välja = silu_andmed(data, n)

päev = [i for i in range(1, len(aeg) + 1)]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(päev, sisse)
ax.plot(päev, välja)
ax.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
ax.set_xlim(1, len(aeg) + 50)
plt.show()