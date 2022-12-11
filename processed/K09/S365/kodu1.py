from statistics import harmonic_mean
import matplotlib.pyplot as plt

nimi = input("mis on andmefaili nimi? ")

fail = open(nimi, 'r', encoding="utf-8")
järj = []
for i in fail:
    i = i.strip().split(", ")
    järj.append(float(i[1]))

fail.close()

def silu_andmed(järj, x):
    arvutatakse =[]
    väljastatakse = []
    for i in range(0, len(järj)):
        if i < x:
            arvutatakse.append(järj[i])
            y = harmonic_mean(arvutatakse)
            väljastatakse.append(y)
        if i >= x:
            arvutatakse.pop(0)
            arvutatakse.append(järj[i])
            y = harmonic_mean(arvutatakse)
            väljastatakse.append(y)
    return väljastatakse
            
#andmed = silu_andmed(järj, 1)
andmed_2 = silu_andmed(järj, 50)

#plt.plot(andmed)
plt.plot(andmed_2)
plt.ylabel("numbrid")
plt.show()