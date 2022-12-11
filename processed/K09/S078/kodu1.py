import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, n):
    
    vp=[]
    vastus=[]
    
    for i in järjend:
        vp.append(i)
        if len(vp) > n:
            vp.pop(0)
        vastus.append(harmonic_mean(vp))
    return vastus
        
print(silu_andmed([2, 1, 3, 4, 5], 3))

andmed = []
aktsiad = []
aeg = []

file = open("aktsiad.txt", "r")
for rida in file:
    andmed = rida.strip().split(",")
    aeg.append(andmed[0])
    aktsiad.append(float(andmed[1]))
file.close()

algandmed = aktsiad
silutud = silu_andmed(aktsiad, 50)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(aeg, algandmed)
ax.plot(aeg, silutud)
ax.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
ax.set_xlim(1, len(aeg) + 50)
plt.show()