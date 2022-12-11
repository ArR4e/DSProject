from statistics import harmonic_mean
import matplotlib.pyplot as plt
fail = open("aktsiad.txt", "r")
failiread = []
nummerdus =[]
p=1
for rida in fail:
    failiread.append(float(rida.strip("\n").split(" ")[3]))
    nummerdus.append(p)
    p+=1
def silu_andmed(jarjend, n):
    uus=[]
    lõplik=[]
    for indx, var in enumerate(jarjend):
        for i in range(n):
            mitmes = indx-i
            if mitmes >= 0:
                uus.append(jarjend[mitmes])
            else:
                break
        lõplik.append(harmonic_mean(uus))
        uus.clear()
    return(lõplik)
        
keskenda = silu_andmed(failiread, 50)

print(nummerdus)

fig = plt.figure()
ax = fig.add_subplot(1,1,1) 

ax.plot(nummerdus, failiread)
ax.plot(nummerdus, keskenda)



plt.show()                   # Kuvame joonise ekraanile.

                   