from statistics import harmonic_mean
import csv
import matplotlib.pyplot as plt

data = dict()
with open("aktsiad.txt", encoding="UTF-8") as f:
    spamreader = csv.reader(f, delimiter=',')
    counter = 0
    for row in spamreader:
        data[counter] = float(row[1].strip())
        counter += 1

def silu_andmed(l, n):
    avg = list()
    for i in range(len(l)):
        if n > i:
            avg.append(harmonic_mean(l[0:i+1]))
        else:
            avg.append(harmonic_mean(l[i-n+1:i+1]))

    return avg

plt.grid(True, linewidth=0.5, color='gray', linestyle='-', axis='y', alpha=.5)
plt.plot(list(data.keys()), list(data.values()), 'r-',color='blue')
plt.plot(list(data.keys()), silu_andmed(list(data.values()), 50), 'r-', color='green')

plt.show()