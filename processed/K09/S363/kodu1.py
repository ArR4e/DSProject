import matplotlib.pyplot as plt
import matplotlib as mpl

from statistics import harmonic_mean as harmooniline
sisend = input("Palun sisesta faili nimi: ")
f = open(sisend)

def silu_andmed(hinnad, n):
    harmoonilised = []
    t = []
    a = 0
    while a < n-1 and a < len(hinnad):
        t.append(hinnad[a])
        harmoonilised.append(harmooniline(t))
        a += 1
        
    while a < len(hinnad):
        t.append(hinnad[a])
        harmoonilised.append(harmooniline(t))
        t.pop(0)
        a += 1
        
    return harmoonilised

kuupäevad = []    
hinnad = []
indeksid = []
s = 0

for rida in f:
    info = rida.split(",")
    kuupäevad.append(info[0])
    hinnad.append(float(info[1].strip()))
    indeksid.append(s)
    s+=1

harmoonilised = silu_andmed(hinnad, 50)

maksimum_a = max(hinnad)
maksimum_b = max(harmoonilised)
tickid = []
k = 0
if maksimum_a > maksimum_b:
    while k <= maksimum_a:
        tickid.append(k)
        k += 0.0025
    tickid.append(k)
        
else:
    while k <= maksimum_b:
        tickid.append(k)
        k += 0.0025
    tickid.append(k)

    
mpl.style.use("default")
objekt = plt.figure()
joonestik = objekt.add_subplot(1,1,1)
joonestik.plot(indeksid, hinnad)
joonestik.plot(indeksid, harmoonilised)
joonestik.plot
joonestik.set_yticks(tickid)

plt.show()



        
    
        