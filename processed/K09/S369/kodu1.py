from statistics import harmonic_mean
import matplotlib.pyplot as plt


f = open('aktsiad.txt')

#silumata andmed
s = []
kuupäevad = []
for rida in f:
    
    päev = rida.split(',')[0].strip()
    kuupäevad.append(päev)
    
    hind = rida.split(', ')[1].strip()
    s.append(float(hind))
    
    
###########################################


def silu_andmed(andmed, n):
    
    t = []
    j = 1
    
    for i in andmed:
        while j < n:
            t.append(harmonic_mean(andmed[0:j]))
            j += 1
    for i in andmed:
        t.append(harmonic_mean(andmed[0:j]))
        andmed.pop(0)
    return t

silutud_andmed = silu_andmed(s, 50)




plt.plot(silutud_andmed)
plt.plot(s)
plt.show()
