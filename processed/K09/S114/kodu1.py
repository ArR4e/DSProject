from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimekiri = []

def silu_andmed(järjend,täisarv):
    i = 0
    JärjendiKoopia = järjend[:]
    JärjendiKoopia2 = järjend[:]
    järjend.clear()
    if len(JärjendiKoopia) >= 1:
        while True:
            if i == 0:
                järjend.append(JärjendiKoopia[0])
            elif i != täisarv:
                arvud = JärjendiKoopia2[:i+1]
                järjend.append((harmonic_mean(arvud[0:len(arvud)])))
            if i == täisarv:
                JärjendiKoopia2.pop(0)
                arvud = JärjendiKoopia2[:täisarv]
                järjend.append((harmonic_mean(arvud[0:len(arvud)])))
            JärjendiKoopia.pop(0)
            if i != täisarv:
                i += 1
            if len(JärjendiKoopia) == 0:
                break
            
    return järjend
        
#failinimi = input("Sisesta algandmete faili nimi: ")
failinimi= "aktsiad.txt"
f1=open(failinimi,"r")
sisu = f1.read().replace("\n",",").split(",") #listiks tegemine
f1.close()
i = 0
while i < len(sisu): #Kuupäevade ja muude asjade eemaldamine
    sisu.pop(i)
    i+=1

uussisu = []

for a in sisu: #Numbrite muutmine listis floatiks
    float(a)
    uussisu.append(float(a))
järjend2 = uussisu[:]


#silu_andmed([1.2,3.4,5.6,7.8],2)
arv = 50

#Graafiku loomine
xtelg = [list(range(len(järjend2)))]
ytelg = [silu_andmed(uussisu,arv)]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(xtelg,ytelg)
#ax.set_ylim(min(järjend2),max(järjend2)) #Y telje väärtused
#ax.set_xlim(0,1000)
plt.show()
 

