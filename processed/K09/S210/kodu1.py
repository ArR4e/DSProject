from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(jär, n):
    jär2 = []
    jär3 = []
    for el in range(len(jär)):
        for i in range(n):
            s = el - i
            if s >= 0:
                jär2.append(jär[s])
            else:
                break
        jär3.append(harmonic_mean(jär2))
        jär2.clear()
    return jär3
f = open("aktsiad.txt", "r")
järjend_numbrid = []
h = 1
jär4 = []
for rida in f:
    jär4.append(float(rida.strip("\n").split(" ")[-1]))
    järjend_numbrid.append(h)
    h+=1
keskmised_andmed = silu_andmed(jär4,50)
fig = plt.figure()
ax= fig.add_subplot(1,1,1)
ax.plot(järjend_numbrid, jär4)
ax.plot(järjend_numbrid, keskmised_andmed)
plt.show()
f.close()