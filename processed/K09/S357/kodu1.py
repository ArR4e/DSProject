from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    a = []
    x = 0
    index = 0
    for el in järjend:
        if index < n:
            a.append(harmonic_mean(järjend[0: x+1]))
            x += 1
        else:
            a.append(harmonic_mean(järjend[index - n: x]))
            x += 1
            n += 1
        index += 1
    return a

f = open("aktsiad.txt", "r")

järjend = []
for line in f:
    c = line.strip().split(",")
    järjend.append(float(c[1]))
 
fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.plot(silu_andmed(järjend, n))
ax.plot(järjend)

plt.show()

f.close()






