f=open("taksohinnad.txt")
teepikkus=float(input("Sisesta tee pikkus kilomeetrites: "))
taksode_hinnad=[]
firma=[]
for rida in f:
    rida=rida.split(',')
    alustus=float(rida[1])
    km_hind=float(rida[2])
    summa=alustus+teepikkus*km_hind
    taksode_hinnad.append(summa)
    firma.append(rida[0])
odavaim=min(taksode_hinnad)
indeks=taksode_hinnad.index(odavaim)
taksofirma=firma[indeks]
print(taksofirma)

f.close()