import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(hinnad, arv):
    uus = []
    vahepealne = []
    for a in hinnad:
        vahepealne.append(a)
        if len(vahepealne) > arv:
            vahepealne.remove(vahepealne[0])
        #print(vahepealne)
        keskmine = harmonic_mean(vahepealne)
        #print(keskmine)

        uus.append(keskmine)   
    return uus

f = open('aktsiad.txt', 'r')
hinnad = []
kuupaevad = []
for a in f:
    a = a.strip()
    a = a.split(', ')
    hinnad.append(float(a[-1]))
    kuupaevad.append(a[0])
    
#print(hinnad)

#hinnad = [2, 1, 3, 4, 5]
n = silu_andmed(hinnad, 50)
#print(n)
tühi = []
korda = 1
for a in kuupaevad:
    tühi.append(korda)
    korda+=1
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(hinnad, korda)
ax.set_xlabel('Hinnad')

ax.set_ylim(0.00000,0.00999)
ax.set_xticks(0, 1020)
plt.show()