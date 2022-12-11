from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(m,n):
    lst1=[]
    for i in range(len(m)):
        s=m[i:i+n]
        hm=harmonic_mean(s)
        lst1.append(hm)
    return lst1
inp=input("Sisesta lähtefaili nimi: ")
f=open(inp, "r")
lst2=[]
for rida in f:
    rida=rida.split(",")
    lst2.append(float(rida[1]))
lst3=silu_andmed(lst2,50)
f.close()
plt.plot(lst3)
plt.plot(lst2)
plt.show()