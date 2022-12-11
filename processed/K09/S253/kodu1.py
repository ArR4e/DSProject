import matplotlib.pyplot
from statistics import harmonic_mean

f = open("aktsiad.txt", "r+", encoding="UTF-8")

def silu_andmed(jarjend, n):
    temp_list = []
    temp = 0
    temp_n = 0
    for i in range(len(jarjend)):
        temp_temp = 0
        temp = harmonic_mean(jarjend[i-temp_n:i+1])
        if temp_n < n-1:
            temp_n += 1
        temp_list.append(temp)
    return temp_list

jarjend1 = []

for rida in f:
    andmed = rida.strip().split(", ")
    jarjend1.append(float(andmed[1]))
jarjend2 = silu_andmed(jarjend1, 50)

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(jarjend1)
ax.plot(jarjend2)
ax.set_xlabel("n")

matplotlib.pyplot.show()   
