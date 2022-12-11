import matplotlib.pyplot as plt

def silu_andmed(jarjend, k):
    uus_jarjend = []
    for i in range(len(jarjend)):
        if i+1 < k:
            murru_peal = i+1
            murru_all = 0
            eelmised = jarjend[:i+1]
            for j in eelmised:
                murru_all += j ** (-1)
            elem = murru_peal / murru_all
            uus_jarjend.append(elem)
        else:
            murru_peal = k
            murru_all = 0
            eelmised = jarjend[i+1-k:i+1]
            for j in eelmised:
                murru_all += j ** (-1)
            elem = murru_peal / murru_all
            uus_jarjend.append(elem)
    return uus_jarjend

paev = []
aktsia = []
f = open("aktsiad.txt", encoding="utf-8")

for rida in f:
    jupid = rida.split(",")
    aktsia.append(float(jupid[1]))
    paev.append(len(aktsia))
    
aktsia_silutud = silu_andmed(aktsia, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(paev, aktsia)
ax.plot(paev, aktsia_silutud)


plt.show()
    
    
