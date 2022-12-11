from matplotlib import pyplot as plt
from statistics import harmonic_mean

def silu_andmed(jär,n):
    jär2=[]
    for X in range(len(jär)):
        X+=1
        if n > X:
            lisatav=[]
            for i in range(X):
                lisatav.append(jär[i])
            jär2.append(harmonic_mean(lisatav))
        else:
            lisatav=[]
            for i in range(n):
                lisatav.append(jär[X-1-i])
            jär2.append(harmonic_mean(lisatav))
    return jär2
def puhastaja(megaruum):
    val=[]
    for line in megaruum:
        val.append(float(line.split(",")[-1].strip()))
    return val

f = open(input("Faili nimi: "))
n=50
algsed= puhastaja(f)
plt.plot(algsed,color= "blue")

plt.plot(silu_andmed(algsed,n),color= "red")

plt.show()
f.close()