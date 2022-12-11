from statistics import harmonic_mean
import matplotlib.pyplot as plt
f = open('aktsiad.txt')

järjend = []
for line in f:
    lineUus = line.split()
    järjend += [float(lineUus[3])]

def silu_andmed(järjend, arv):
    vastus = []
    suurus = range(len(järjend))
    for el in suurus:
        if  el < arv:
            algus = 0
        else:
            algus = el-arv+1
        vastus += [harmonic_mean(järjend[algus:el+1])]
    return vastus

päevad = []
for el in range(len(järjend)):
    päevad += [el]
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, järjend)
ax.plot(päevad, silu_andmed(järjend, 50))
ax.set_xlabel("Päevad")
plt.show()

f.close()