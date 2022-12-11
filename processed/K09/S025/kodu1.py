from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    i = 0
    jär = []
    for i in range(len(järjend)):
        if i == 0:
            a = [järjend[i]]
            jär.append(float(harmonic_mean(a)))
            i += 1
        elif i >= n-1:
            b = järjend[i-(n-1):i-(n-1)+n]
            jär.append(float(harmonic_mean(b)))
            i += 1
        elif 0 < i < n-1:
            c = järjend[0:i+1]
            jär.append(float(harmonic_mean(c)))
    return jär

f = open(input('Sisesta faili nimi: '))
aktsiad = []
for rida in f:
    aktsiad.append(float(rida.strip('\n').split(', ')[1]))
plt.plot(aktsiad)
plt.plot(silu_andmed(aktsiad, 50))
plt.show()
f.close()