from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j,n):
    k=[]
    for i in range(len(j)):
        if i<n-1:
            k.append(harmonic_mean(j[0:i+1]))
        else:
            k.append(harmonic_mean(j[i-n+1:i+1]))
    return k

f=open("aktsiad.txt")
t=f.readlines()
a=[]
for i in range(len(t)):
    a.append(float(t[i].split(",")[-1]))
f.close()
b=silu_andmed(a,50)
print(b)
plt.plot(range(len(b)),b)
plt.plot(range(len(a)),a)
plt.show()