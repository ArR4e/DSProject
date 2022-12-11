from statistics import harmonic_mean

nimi = input("Sisesta faili nimi: ")
fail = open(nimi, "r", encoding="UTF-8")

andmed = fail.readlines()
fail.close()

n = int(input("Mitme elemendi kaupa keskmistada: "))

def silu_andmed(andmed, n):
    lst = []
    arvutus_lst = []
    h_m_lst = []
    for i in range(len(andmed)):
        rida = andmed[i].strip().split(", ")
        lst.append(rida)
    
    for i in range(len(lst)):
        if i < n:
            arvutus_lst.append(float(lst[i][1]))
            h_m = harmonic_mean(arvutus_lst)
            h_m_lst.append(h_m)
        else:
            arvutus_lst.append(float(lst[i][1]))
            arvutus_lst.pop(0)
            h_m = harmonic_mean(arvutus_lst)
            h_m_lst.append(h_m)
        
    return h_m_lst
        
        
silutud = silu_andmed(andmed,n)




kuud = []
for i in range(len(silutud)):
    kuud.append(i)

algandmed = []
for i in range(len(andmed)):
    algandmed.append(float(andmed[i].split(", ")[1].strip()))

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(kuud, silutud)
ax.plot(kuud, algandmed)
ax.set_xlabel("Kuud")
ax.set_ylabel("Hinnad")

plt.show()