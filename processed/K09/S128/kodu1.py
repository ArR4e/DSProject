#Andmete silumine
from statistics import harmonic_mean
import matplotlib.pyplot as plt

fail = open("aktsiad.txt", encoding="UTF-8")
aktsiad = []
vahemik = []
m=1
for rida in fail:
    aktsiad.append(float(rida[13:len(rida)-1]))
    vahemik.append(m)
    m +=1
fail.close()

def silu_andmed(järjend, n):
    keskmistatud = []
    for i in range(0, len(järjend)):
        if i-(n-1) < 0:
            keskmistatud.append(float(harmonic_mean(järjend[0:(i+1)])))
        else:
            keskmistatud.append(float(harmonic_mean(järjend[i-(n-1):(i+1)])))
    return keskmistatud

el_arv = int(input("Sisesta n: "))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(vahemik, aktsiad)  
ax.plot(vahemik, silu_andmed(aktsiad, el_arv))  
plt.show()            
