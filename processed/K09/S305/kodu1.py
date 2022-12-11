from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(b, c):
    
    a = []
    i = 0
    
    for i in range(1, c+1):
        a.append(harmonic_mean(b[0:i]))
        
    for i in range(1, (len(b)-(c-1))):
        a.append(harmonic_mean(b[i:i+c]))
        
    return a
    
fail = open(input("Sisesta faili nimi: "))
arv = []
ar = 0
hind = []

for i in fail:
    h = i.split(", ")
    ar += 1
    arv.append(ar)
    hind.append(float(h[1].strip("\n")))

fail.close()
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(arv, hind)
ax.plot(arv, silu_andmed(hind, n))
ax.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
ax.set_xticks([0, 200, 400, 600, 800, 1000])

plt.show()