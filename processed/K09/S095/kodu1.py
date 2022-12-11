from statistics import harmonic_mean
import matplotlib.pyplot as plt


f=open("aktsiad.txt")
data=[]
for line in f:
    stripped_line=line.strip()
    stripped_line=stripped_line.split(', ')[1]
    data.append(float(stripped_line))

def silu_andmed(arr, n):
    silu=[]
    array=[]
    sm=0
    for i in range(len(arr)):
        array.append(arr[i])
        if len(array)>n:
            array.pop(0)
            sm=harmonic_mean(array)
            silu.append(sm)
        else:
            sm=harmonic_mean(array)
            silu.append(sm)
    return silu

plt.plot(data)
plt.plot(silu_andmed(data, 50))
plt.show()

f.close()