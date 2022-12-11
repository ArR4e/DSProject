import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(jrj, n):                                        #funktsioon
    sile = []
    i = 0
    paluntööta = []
    for el in jrj:
        if i < n:
            paluntööta.append(jrj[i])
            liige = harmonic_mean(paluntööta)
            print(liige)
            sile.append(liige)
            i += 1
        elif i == n:
            paluntööta.pop(0)
            paluntööta.append(jrj[i])
            liige = harmonic_mean(paluntööta)
            sile.append(liige)
            i += 1
        elif i > n:
            paluntööta.pop(0)
            paluntööta.append(jrj[i])
            liige = harmonic_mean(paluntööta)
            sile.append(liige)
            i += 1
    return sile


f = open("aktsiad.txt", "r")                                               #Loeb faili ja teeb listid 
jrj = []
ajajr = []
k = 0
while True:
    a = f.readline().strip().split()   
    if a == []:
        break
    jrj.append(float(a[3]))
    k += 1
    ajajr.append(k)

silejrj = silu_andmed(jrj, 50)

fig = plt.figure()                                            #joonistab
ax = fig.add_subplot(1,1,1)

ax.plot(ajajr, jrj)
ax.plot(ajajr, silejrj)
ax.set_xlabel("Aeg")
plt.show()