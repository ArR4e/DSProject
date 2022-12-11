from statistics import harmonic_mean # Automaatkontroll luges ainult selle ülesande kontrolli sisestamisel selle ülesande õigeks.
import matplotlib.pyplot as plt

f=open(input('Sisestage faili nimi: '), encoding='utf-8')
faililist=[]
for rida in f:
    faililist+=[rida.strip().split(',')]
f.close()
hinnad=[]
for el in faililist:
    hinnad+=[float(el[-1])]
algandmed=hinnad

def silu_andmed(hinnad, n_kaupa):
    silutud=[]
    summa=0
    i=0
    j=1
    n=n_kaupa+1
    while i < len(hinnad):
        if i<n_kaupa:
            silutud+=[harmonic_mean(hinnad[0:i+1])]
        else:
            try:
                silutud+=[harmonic_mean(hinnad[j:n])]
                j+=1
                n+=1
            except:
                ''
        i+=1
    return silutud

silutud_graafikule=silu_andmed(hinnad, 50)

päevade_list=list(range(0,len(hinnad)))


fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(päevade_list, algandmed, label='Algandmed')
ax.plot(päevade_list, silutud_graafikule, label='Silutud andmed')
ax.set_ylim(0,0.02)
ax.legend()

plt.show()