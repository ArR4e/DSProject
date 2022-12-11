from  statistics import harmonic_mean
import matplotlib.pyplot as plt

fail1 = open("aktsiad.txt")
uus_jarjend  = []
for i in fail1:
    i = (i.strip()).split()
    uus_jarjend.append(float(i[3]))
print(uus_jarjend)

mitme_elemendi_kaudu = int(input("Sisesta, mitme elemdi kaudu sa soovikisid andmeid siluda: "))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
    
ax.plot(uus_jarjend)
ax.set_xlabel("Andmed")

def silu_andmed(jarjend,n):
    rida = []
    uus_jarjend1 = []
    loendur = 1
    arv = 0
    for i in jarjend:
        if loendur != n+1:
            rida1 = float(1/i)
            rida.append(rida1)
            arv = 0
            for j in rida:
                arv = arv + j
            k = loendur/arv
            uus_jarjend1.append(k)
            loendur = loendur + 1
        else:
            rida1 = float(1/i)
            rida.append(rida1)
            rida = rida[1:(n+1)]
            arv = 0
            for j in rida:
                arv = arv + j
            tulemus = (loendur-1)/arv
            uus_jarjend1.append(tulemus)
    return uus_jarjend1

ax.plot(silu_andmed(uus_jarjend, mitme_elemendi_kaudu))
plt.show()
