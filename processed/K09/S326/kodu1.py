import matplotlib.pyplot as plt
from statistics import harmonic_mean

algandmed = open(input("Algandmed: "))
järjend = []
for rida in algandmed:
    ridajär = rida.split(",")
    järjend.append(float(ridajär[1].strip()))

def silu_andmed(jär, n):
    while jär != []:
        n_elemendid = []
        for i in jär[-n:]:
            n_element = jär.pop(jär.index(i))
            n_elemendid.append(n_element)
        hm_jär = []
        hm = harmonic_mean(n_elemendid)
        hm_jär.append(hm)
    return hm_jär
silu_andmed([1,2,5,4,3,6,4,3,9], 3)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(järjend)
#ax.plot(silu_andmed(järjend, 50))
plt.show()