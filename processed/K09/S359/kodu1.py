from statistics import harmonic_mean
import matplotlib.pyplot as plt


nimi=str(input("Sisesta faili nimi: "))
arv=int(input("Sisesta täisarv, mis näitab mitme elemendi kaupa keskmistamist rakendatakse: "))
#f=open("aktsiad.txt", "r")
f=open("nimi", "r")
#f=[2, 1, 3, 4, 5]

#[(1/(1/2)),?,?,?,(3/(1/3 + 1/4 + 1/5))]
#plt.plot(arve jarjend)
#plt.show()tühi
#jarjend=[]
def silu_andmed(xoxox,arv):
    jarjend=[]
    #l=harmonic_mean(xoxox)
    #jarjend.append(l)
    for indeks in range(1,len(xoxox)+1):
        algus= max(0, indeks-arv)
        j=harmonic_mean(xoxox[algus:indeks])
        jarjend.append(j)
    return jarjend

funktsiooni=[]

for i in f:
    strip = i.strip()
    split = strip.split()
    viimane=split.pop()
    funktsiooni.append(viimane)
    
funktsiooni = list(map(float, funktsiooni))

peeter=(silu_andmed(funktsiooni,arv))

#ehk ss silu_andmed(funktsiooni, arv) ning funktsiooni

plt.plot(funktsiooni)
plt.plot(peeter)
plt.show()
