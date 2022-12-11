from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(h, n):
    silutud = []
    num = []
    a = 1
    for i in range(0,len(h)):
        num.append(float(h[i]))
        silutud.append(harmonic_mean(num))
        if len(num) >= n:
            num.pop(0)
    return silutud

filename = str(input("--->"))


with open(filename, "r", encoding="utf-8") as f:
    data = []
    for i in f:
        i = i.split(",")
        data.append(float(i[1].strip()))
        


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(data)
ax.set_xlabel("harm.keskmine")
ax.plot(silu_andmed(data, 50))

plt.show()
 
