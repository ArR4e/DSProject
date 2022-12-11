from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(andmed, n):
    keskmistatud = []
    for i in range(len(andmed)):
        if i+1<=n:
            keskmistatud.append(harmonic_mean(andmed[0:i+1]))
        elif i+1>n:
            keskmistatud.append(harmonic_mean(andmed[i-n+1:i+1]))
    return keskmistatud

print(silu_andmed([2, 1, 3, 4, 5],3))

f = open(input("Sisestage faili nimi: "))
lines = f.readlines()
linesplits = []
for el in lines:
    linesplits.append(el.strip().split(", "))
f.close()
i = 0
j = 0
paevad = []
aktsiad = []
for line in linesplits:
    for el in line:
        if j%2==0:
            paevad.append(j)
            j+=1
        elif j%2 != 0:
            aktsiad.append(float(el))
            j+=1
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(paevad, aktsiad)
ax.set_xlabel("Päevad")

ax.plot(paevad, silu_andmed(aktsiad, 50))

ax.set_ylim(0, max(aktsiad)*1.1)
ax.set_xticks(paevad)


plt.show()