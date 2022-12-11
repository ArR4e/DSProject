def thind(algus, kmhind, km):
    algus=float(algus)
    kmhind=float(kmhind)
    hind=0
    hind=algus+km*kmhind
    return hind

firmad=[]
hinnad=[]
distants=float(input("Sisesta tee pikkus kilomeetrites: "))

f=open("taksohinnad.txt", "r")
for rida in f:
    rida=rida.strip()
    rida=rida.split(",")
    firmad.append(rida[0])
    taksohind=thind(rida[1],rida[2],distants)
    hinnad.append(taksohind)
f.close()
try:
    indeks=hinnad.index(min(hinnad))
    print("Kõige odavam on "+firmad[indeks]+".")
except:
    print("Ei leidnud hinda")