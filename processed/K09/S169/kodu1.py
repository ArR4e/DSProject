from statistics import harmonic_mean as hm
import matplotlib.pyplot as plt

def silu_andmed(list,n):
    hm_list = []
    for a in range(len(list)):
        if a-n < 0:
            m = 0
        else:
            m = a-n+1
        hm_list.append(hm(list[m:a+1]))
        
        
        
    return hm_list
    
f = input("Sisesta faili nimi: ")
fail = open(f,"r",encoding="utf-8")
list = []
for a in fail.readlines():
    list.append(float(a.split(",")[1].strip()))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(list)
ax.plot(silu_andmed(list, 50))
plt.ylabel("Aktsia väärtus")
plt.show()