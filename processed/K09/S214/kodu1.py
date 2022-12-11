from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend,arv):
    uus_järjend = []
    i = 0
    if arv == 1:
        return järjend
    for element in järjend:
        if i <= arv-1:
            uus_järjend +=[harmonic_mean(järjend[0:i+1])]
            i += 1
        else:
            if i<= len(järjend):
                uus_järjend += [harmonic_mean(järjend[i-arv+1:i+1])]
                i+=1
    return uus_järjend

print(silu_andmed([5.93,4.56,3,2.62,1],1))
failinimi = input("Sisesta failinimi: ")
f = open(failinimi)
aktsiad = []
a = 1
päevi = []
for rida in f:
    aktsiad += [float(rida.strip()[13:])]
    päevi += [a]
    a +=1
silutud = silu_andmed(aktsiad,50)

plt.plot(päevi,aktsiad,"-", label = "Algne")
plt.plot(silutud,"-",label = "Silutud")
plt.legend()
plt.show()