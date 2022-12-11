from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    silutud = []
    for i in range(1,len(järjend)+1):
        if i < n:
            silutud.append(harmonic_mean(järjend[0:i]))
        else:
            silutud.append(harmonic_mean(järjend[i-n:i]))
    return silutud

sisend = input("Sisestage failinimi: ")
f = open(sisend,"r",encoding = "UTF-8") 
n = 50

aktsiad = []
while True:
    rida = f.readline()
    if rida == "":
        break
    
    aktsiad.append(float(rida[13:]))

silutud = silu_andmed(aktsiad,n)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(range(len(aktsiad)), aktsiad, label = "silumata")
ax.plot(range(len(silutud)), silutud, "r-", label = "silutud")

ax.legend()
plt.show()

#print(silu_andmed([2, 1, 3, 4, 5],3))