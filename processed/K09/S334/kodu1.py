from statistics import harmonic_mean
import matplotlib.pyplot as plt 

def silu_andmed(mylist, n):
    temp = []
    i = 0
    x = 0
    while x in range(len(mylist)):
        if i < n:
            temp.append(harmonic_mean(mylist[0:i+1]))
            i += 1
        if i >= n and i <= len(mylist) - 1:
            temp.append(harmonic_mean(mylist[i-n+1:i+1]))
            i += 1
        x += 1

    return temp

jarj = []
with open("aktsiad.txt") as f:
    for item in f.readlines():
        jarj.append(item.strip().split(', ')[1])
jarj = list(map(float, jarj))

silutud_jarj = (silu_andmed(jarj, 50))

###GRAAFIK###

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(jarj)
ax.plot(silutud_jarj)
plt.show()