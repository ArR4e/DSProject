from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed_järjendina, täisarv):
    vastus=[]
    a=0
    b=[]
    while a < (täisarv-1) and a<len(algandmed_järjendina):
        otsitav=algandmed_järjendina[a]
        b.append(otsitav)
        harmooniline_keskmine=harmonic_mean(b)
        vastus.append(harmooniline_keskmine)
        a+=1
    
    if täisarv>=len(algandmed_järjendina):
        return vastus
    else:
        viimase_teguri_indeks=täisarv-1
        muutuja=1
        while True:
            viimane_tegur=algandmed_järjendina[viimase_teguri_indeks]
            üks_harmooniline_keskmine=[]
            üks_harmooniline_keskmine.append(viimane_tegur)
            muutuja=1
            while muutuja<=(täisarv-1):
                ajutine_indeksikene=((viimase_teguri_indeks)-muutuja)
                üks_harmooniline_keskmine.append(algandmed_järjendina[ajutine_indeksikene])
                muutuja+=1
            viimase_teguri_indeks+=1
            if viimase_teguri_indeks==((len(algandmed_järjendina))):
                harmooniline_keskmine=harmonic_mean(üks_harmooniline_keskmine)
                vastus.append(harmooniline_keskmine)
                break
            else:
                harmooniline_keskmine=harmonic_mean(üks_harmooniline_keskmine)
                vastus.append(harmooniline_keskmine)
                continue
        return(vastus)
  
sisend_kasutajalt=input("Sisestage algandmete faili nimi ")
fail=open(sisend_kasutajalt,"r",encoding="utf-8")
algandmed_järjendina=[]
faili_sisu=[]
for rida in fail:
    osad=rida.split(",")
    for osa in osad:
        faili_sisu.append(osa.strip("\n"))

a=1
for element in faili_sisu:
    lisatav=float(faili_sisu[a])
    algandmed_järjendina.append(lisatav)
    a+=2
    if a <= len(faili_sisu):
        continue
    else:
        break
ridade_arv=[]
a=0
while a<len(algandmed_järjendina):
    ridade_arv.append(a)
    a+=1
    
vastus=silu_andmed(algandmed_järjendina, täisarv)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(ridade_arv, vastus)
ax.plot(ridade_arv, algandmed_järjendina)
plt.show()