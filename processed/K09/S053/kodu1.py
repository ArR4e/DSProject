from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, täisarv):
    keskmistatud_andmed = []
    keskmistatud_andmed.append(float(järjend[0]))
    i = 1
    for i in järjend:
        while i != täisarv:
            a = harmonic_mean(järjend[0:1+1])
            i += 1
            keskmistatud_andmed.append(a)
        else:
            järjend.pop(0)
            if täisarv > len(järjend):
                break
            a = harmonic_mean(järjend[0:täisarv])
            keskmistatud_andmed.append(a)
    print(keskmistatud_andmed)


failinimi = input("Sisestage failinimi: ")
f = open(failinimi, "r", encoding = "utf-8")
algandmed = []
for el in f:
    eraldi = el.split(", ")
    hind = eraldi[-1]
    ilmaNita = hind.strip("\n")
    algandmed.append(ilmaNita)
ujukomaarvudena_algandmed = list(map(float, algandmed))

f.close()

täisarv = int(input("Sisesta täisarv: "))
keskmistatud_andmete_järjend = []
b = silu_andmed(ujukomaarvudena_algandmed, täisarv)
keskmistatud_andmete_järjend.append(b)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(ujukomaarvudena_algandmed, keskmistatud_andmete_järjend)        

ax.set_ylim(0, 0.0175, 0.0025)         
ax.set_xticks([0, 200, 400, 600, 800, 1000]) 

plt.show() 