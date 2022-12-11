import statistics
import matplotlib.pyplot as plt
f = open(input("Sisestafaili nimi: "), "r")
n = int(input("Sisesta arv: "))

#f = open("aktsiad.txt", "r")
#n = 3


uus_järjend = []
for i in f:
    rida = i.split(" ")
    järjend = rida[3].strip()
    järjend_2 = järjend.split()
    uus_järjend = uus_järjend + järjend_2

def silu_andmed(x, n):
    pikkus = len(x)
    print(pikkus)
    arv_jada = []
    j = 0
    while j < pikkus - n:
        
        tühi = []
        u = 0
        while u < n:
            tühi.append(float(x[j + u]))
            u += 1
        arv = statistics.harmonic_mean(tühi)
        return arv
        j += 1
    arv_jada = arv_jada + arv
    return arv_jada
        #return arv
        #print(arv)
        
print(silu_andmed(uus_järjend, n))
#silu_andmed(uus_järjend, n)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.plot(uus_järjend)
plt.plot(silu_andmed(uus_järjend, n))
ax.set_ylim(0,max(uus_järjend))

plt.show()

#print(statistics.harmonic_mean(uus_järjend))
          