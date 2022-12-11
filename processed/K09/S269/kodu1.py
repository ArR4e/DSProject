from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    silu = järjend.copy()
    if len(järjend) > n:
        for i in range(len(järjend) - n):
            silu[-i-1] = harmonic_mean(silu[-i-1:-i-n-1:-1])
        for j in range(n-1, -1, -1):
            silu[j] = harmonic_mean(silu[:j+1])
    else:
        for k in range(len(järjend)-1, -1, -1):
            silu[k] = harmonic_mean(järjend[:k+1])
    return silu

with open(input("Algandmete faili nimi: ")) as f:
    alg = []
    for rida in f:
        alg.append(float(rida.split(",")[-1].strip()))
    silutud = silu_andmed(alg, 50)
    plt.plot(alg)
    plt.plot(silutud)
    plt.show()