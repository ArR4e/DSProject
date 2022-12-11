from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(arr, n):
    uus = []
    for i in range(len(arr)):
        if i >= n:
            uus.append(harmonic_mean(arr[i-n+1:i+1]))
        else:
            uus.append(harmonic_mean(arr[:i+1]))
    return uus

f = open("aktsiad.txt", "r")
paevad = []
aktsiad = []

for i in f.readlines():
    sisend = i.split(",")
    paevad.append(sisend[0])
    aktsiad.append(float(sisend[1].strip()))

n = 50

plt.plot(paevad, aktsiad)
plt.plot(paevad, silu_andmed(aktsiad, n))
plt.xticks(list(range(len(paevad)))[0:len(paevad):200])
plt.show()
#print(silu_andmed(aktsiad,n))