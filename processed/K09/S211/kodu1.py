from statistics import harmonic_mean
import matplotlib.pyplot as plt


def silu_andmed(järjend, n):
    silutud = järjend.copy()
    
    for i in range((len(silutud))):
        if i==0:
            silutud[i]= järjend[i]
        elif (i-n) < 0:
            silutud[i] = harmonic_mean(järjend[0:(i+1)])
        else:
             silutud[i] = harmonic_mean(järjend[(i-n+1):i+1])
    return(silutud)

sisend = input("Sisesta algandmete faili nimi: ")

akt = open(sisend, "r")
aktsiate_hinnad = []
for rida in akt: #aktiate hindadest järjend
    ühe_kaupa = rida.split()
    aktsiate_hinnad.append(float(ühe_kaupa[3]))

plt.plot(aktsiate_hinnad)
plt.ylabel("Hinnad")
plt.plot(silu_andmed(aktsiate_hinnad, 50))

plt.show()