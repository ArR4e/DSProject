from statistics import harmonic_mean
print(harmonic_mean([3, 4, 5]))
silutudjärjend=[]
def silu_andmed(järjend, n):
    for element in järjend:
        if n > 0:
            silutudelement = järjend[element]
            silutudjärjend.append(silutudelement)
            n -= 1
    harmoonia = harmonic_mean(silutudjärjend)
silu_andmed([2, 1, 3, 4, 5], 3)
    