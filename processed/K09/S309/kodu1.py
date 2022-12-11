
from statistics import  harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(listvar, var):
    n = []
    h = 0
    for index,item in enumerate(listvar):
        if h < var:
            n.append(float(harmonic_mean(listvar[0:index+1])))
        if h >= var:
            n.append(float(harmonic_mean(listvar[index-var+1:index+1])))
        h += 1

    return n

filename = str(input("Sisetage failnimi:"))
data = []
datedata = []
with open(filename, "r", encoding="UTF-8") as file:
    for line in file:
        linedata = line.split(",")
        data.append(float(linedata[1]))
        datedata.append(str(linedata[0]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel("Aeg")
ax.set_ylabel("Aktsiahind")

ax.plot(data)
ax.plot(silu_andmed(data,50))

plt.show()