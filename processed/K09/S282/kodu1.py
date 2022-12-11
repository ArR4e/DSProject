from statistics import harmonic_mean
import matplotlib.pyplot as plt

n=int(input('Sisestage n väärtus: '))
fail= open(input("Sisestage faili nimi: "))

hinnad=[]
for el in fail:
    hinnad.append(float(el[13:21]))
    
def silu_andmed(hinnad,n):
    n_hinnad=[]
    harmoonilised_keskmised=[]
    m=0
    for el in hinnad:
        m+=1
        n_hinnad.append(el)
        harmoonilised_keskmised.append(harmonic_mean(n_hinnad))
        if m>=n:
            n_hinnad.pop(0)
    return harmoonilised_keskmised

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(hinnad)
ax.plot(silu_andmed(hinnad,n))
plt.show()
        
