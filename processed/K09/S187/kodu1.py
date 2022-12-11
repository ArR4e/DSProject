from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(andmed, n):
    uued_andmed = []
    for i in range(0, len(andmed)):
        if i < n:
            x = harmonic_mean(andmed[:i + 1])
            uued_andmed.append(x)
        else:
            x = harmonic_mean(andmed[i - n + 1: i + 1])
            uued_andmed.append(x)
    return(uued_andmed)

fail = input("Sisesta faili nimi: ")
f = open(fail, "r")

hinnad = []
for rida in f.readlines():
    rida = rida.split(",")
    hinnad.append(float(rida[1].strip()))

f.close()

x_rida = range(len(hinnad))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x_rida, hinnad, color = "blue")
ax.plot(x_rida, silu_andmed(hinnad, 50), color = "red")

plt.show()