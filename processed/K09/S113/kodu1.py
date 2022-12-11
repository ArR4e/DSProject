import matplotlib.pyplot as plt
from statistics import harmonic_mean
nimi = input("Sisesta failinimi:")
fail = open(nimi + ".txt", "r", encoding="UTF-8")
j = []
for rida in fail:
    e = rida.strip()
    s = e.split(" ")
    u = float(s[-1])
    j.append(u)
def silu_andmed(j, n):
    global jär
    jär = []
    for indeks in range(1, len(j) + 1):
        algus = max(0, indeks - n)
        kesk = harmonic_mean(j[algus:indeks])
        jär.append(kesk)
    return jär
uus = silu_andmed(j, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(j)
ax.plot(uus)
plt.show()
fail.close()
