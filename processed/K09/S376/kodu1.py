from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(j, n):
    silutud = []
    silutav = []

    for i in range(len(j)):
        silutav += [j[i]]
        
        if len(silutav) >= n+1:
            silutav.pop(0)
        
        silutud += [harmonic_mean(silutav)]
        
    return silutud

aktsiad = []
päevad = []
p = 0

sisend = input("Sisesta faili nimi: ")

with open(sisend) as f:
    for rida in f:
        rida = f.readline().strip().split(", ")
        if rida == [""]:
            break
        else:
            päevad += [p]
            p += 1
            aktsiad += [rida[1]]

for i in range(0, len(aktsiad)):
    aktsiad[i] = float(aktsiad[i])
    
andmed = silu_andmed(aktsiad, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, aktsiad)
ax.plot(päevad, andmed)
ax.set_xlabel("Kuud")
plt.show()