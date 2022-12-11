from random import randint
import copy
def minu_shuffle(a): 
    indeksi_pikkus=len(a)
    uus_indeks=[]
    b=copy.deepcopy(a) #koht mille põhjal täidame uuesti a
    vana_indeks=[]
    i=indeksi_pikkus
    for e in range(0,indeksi_pikkus):
        vana_indeks+=[e]
        #print(str(vana_indeks) + "vana indeksi loomine")
    while i>0:
        n=randint(0, indeksi_pikkus-1)
        if n not in uus_indeks:
            uus_indeks+=[n]
            i-=1
        #print(str(uus_indeks)  + "uue indeksi loomine")
    for el in range(0,indeksi_pikkus):
        a[vana_indeks[0]]=b[uus_indeks[0]]
        #print(str(uus_indeks)  + "uue indeksi muutmine")
        #print(str(vana_indeks)  + "vana indeksi muutmine")
        #print(str(a) + "uus asi")
        del uus_indeks[0]
        del vana_indeks[0]
