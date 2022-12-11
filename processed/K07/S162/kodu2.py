f=open('taksohinnad.txt')
tee=float(input("mitu kilomeetrit soovid sõita? "))
nimed=[]
hinnad=[]
for rida in f:
    rida=rida.split(',')
    nimi=rida[0]
    hind=float(rida[1])+tee*float(rida[2])
    hinnad.append(hind)
    nimed.append(nimi)
odavaim=min(hinnad)
indeks=hinnad.index(odavaim)
    
print("odavaim variant on",nimed[indeks])
    #ok ma annan alla lmao mul pole enam ühtki ideed kuidas seda test4 tööle saada. headööd