from statistics import harmonic_mean
import matplotlib.pyplot as plt
fail = input("Sisesta failinimi: ")
with open(fail) as f:
    a = [float(line.split()[-1]) for line in f]

def silu_andmed(järj, n):
    s = []
    for i in range(len(järj)):
        if i == 0:
            s.append(1/(1/järj[i]))
        elif i < n:
            s.append(harmonic_mean(järj[:i+1]))
        else:
            s.append(harmonic_mean(järj[i-n+1:i+1]))
    return s

fig = plt.figure()
päevad = [x+1 for x in range(len(a))]
ax = fig.add_subplot(1,1,1)
ax.set_xlabel("Päevad")
ax.plot(päevad, a, "-")
ax.plot(päevad, silu_andmed(a, 50), "-")
ax.set_ylabel("Viimase 50 päeva harmooniline keskmine")
plt.show()