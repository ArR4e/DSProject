kilomeetrite_arv=float(input("Sisesta tee pikkus kilomeetrites: "))
f=open("taksohinnad.txt")
hinnad=[]
nimi=[]
for rida in f:
    järjend=rida.split(",")
    firma=järjend[0]
    kilomeetri_hind=float(järjend[2])
    stardihind=float(järjend[1])
    hind = stardihind + kilomeetrite_arv*kilomeetri_hind
    hinnad.append(hind)
    nimi.append(firma)
    väikseim=min(hinnad)
    indeks=hinnad.index(väikseim)
    min_nimi=nimi[indeks]
print("Kõige odavam on",min_nimi)
f.close()