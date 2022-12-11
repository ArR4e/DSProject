import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(järjend, n):
    result = []
    for i in järjend:
        if järjend.index(i) < n:
            arv = järjend[0:järjend.index(i) + 1]
            result.append(float(harmonic_mean(arv)))
        elif n == 1:
            result.append(1/(1/i))
        else:
            arv = järjend[järjend.index(i) - (n - 1):järjend.index(i) + 1]
            result.append(float(harmonic_mean(arv)))
    return result


f = open("aktsiad.txt", "r")
aktsiad = [line.strip().split(', ') for line in f]
f.close()
aktsiad_num = [float(i[1]) for i in aktsiad]
aktsiad_kuud = [i[0] for i in aktsiad]
result = silu_andmed(aktsiad_num, 50)

plt.plot([*range(len(aktsiad_num))], aktsiad_num, label="järjend")
plt.plot([*range(len(result))], result, label="harmooniline keskmine")
plt.legend()
plt.xlabel("index")
plt.show()
   