from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(a,b):
    k = 0
    l = []
    m = []
    for x in a:
        if k < b:
            l.append(a[k])
            m.append(harmonic_mean(l))
            k += 1
        else:
            l.pop(0)
            l.append(a[k])
            m.append(harmonic_mean(l))
            
    return m

