from statistics import harmonic_mean
import matplotlib.pyplot as plt 

def silu_andmed(andmed, n):
    silutud = []
    if n < len(andmed):
        for i in range(n):
            silutud.append(harmonic_mean(andmed[:i+1]))
        for i in range(n,len(andmed)):
            silutud.append(harmonic_mean(andmed[i+1-n:i+1]))
    else:
        for i in range(len(andmed)):
            silutud.append(harmonic_mean(andmed[:i+1]))
    return silutud


fail = open(input("Sisesta fail: "), encoding = "UTF-8")
#fail = open("aktsiad.txt", encoding = "UTF-8")
data = fail.readlines()
#kuupäev = []
hind = []
for line in data[:]:
    line = line.strip().split(",")
    #kuupäev.append(line[0])
    hind.append(float(line[1]))

fail.close()

#hind = [5.93, 4.56, 3, 2.62, 1]

sile = silu_andmed(hind, 1)
#print(sile)


plt.plot(range(len(hind)), hind)
plt.plot(range(len(sile)), sile)
plt.show()


