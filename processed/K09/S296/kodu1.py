import statistics

fail = input("Algandmete fail: ")
fail = open(fail,"r")
aktsiad = []
arv=[]
for rida in fail:
    element1 = rida.strip()
    element2 = element1.split(", ")
    aktsiad.append(float(element2[1]))

for x in range(len(aktsiad)):
    arv.append(x+1)
    
#n = int(input("Sisesta n: "))

def silu_andmed(jär,n):
    i = 1
    uus_jär = []
    for el in jär:
        if i < n:
            el = statistics.harmonic_mean(jär[0:i])
            uus_jär.append(el)
            i += 1
        else:
            el = statistics.harmonic_mean(jär[i-n:i])
            uus_jär.append(el)
            i += 1
    return uus_jär
print(silu_andmed(aktsiad,50))

import matplotlib.pyplot as plt

plt.plot(arv,aktsiad, label="aktsiad")
plt.plot(arv,silu_andmed(aktsiad,n), label="sili_andmed")
plt.xlabel("ma ei tea")

plt.show()