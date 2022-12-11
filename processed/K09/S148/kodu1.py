from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(andmed, n):
    i = 0
    a = []
    b = 0
    c = []
    d = []
    for el in andmed:
        d += [el]
    
    for el in andmed:
        if i < n:
            i += 1
            
            b += 1 / el
            c += [i / b]
        
        elif i == n:
            del d[0]
            
            j = 0
            b = 0
            while j < n:
                b += 1/d[j]
                j += 1
            
            c += [i / b]
    return c

"""
f = open("aktsiad.txt", encoding="UTF-8")

z = 0
xt = []
yt = []
for rida in f:
    info = rida.strip().split(", ")
    z += 1
    xt += [z]
    yt += [info[1]]

f.close()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(xt, yt)

plt.show()
"""