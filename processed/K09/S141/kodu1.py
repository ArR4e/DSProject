fail = open(input("Fail: "), "r")
read = fail.readlines()
fail.close()

algjärjend = []
for el in read:
    arv = el.split(",")
    arv = float(arv[1].strip())
    algjärjend += [arv]
algjärjend1 = algjärjend.copy()

from statistics import harmonic_mean

def silu_andmed(järjend, n):
    uusjärjend = []
    for i in range(1, len(järjend)+1):
        if i <= n:
            arvud = järjend[0:i]
        else:
            järjend.pop(0)
            arvud = järjend[0:n]
        kesk = harmonic_mean(arvud)
        uusjärjend = uusjärjend + [kesk]
    return uusjärjend
    
uusjärjend1 = silu_andmed(algjärjend, n)


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


ax.plot(algjärjend1, "-r")
ax.plot(uusjärjend1, "-b")

ax.set_xticks([0, 200, 400, 600, 800, 1000])

plt.show()