from statistics import harmonic_mean
import matplotlib.pyplot as plt
import re
def silu_andmed(x, n):
    average = []
    for i in range(len(x)):
        sublist = x[max(0, i+1-n):i+1]
        average.append(harmonic_mean(sublist))
    return average

f = open(input('Sisesta algandmete faili nimi: '), encoding='utf-8')
line = f.readline()
algandmed = []
while line:
    algandmed.append(float(re.sub(r'^.*?, ', '', line)))
    line = f.readline()
f.close()
silutud = silu_andmed(algandmed, 50)

fig = plt.figure()
ala = fig.add_subplot(1, 1, 1)
ala.plot(algandmed)
ala.plot(silutud)
plt.show()