f = open("taksohinnad.txt", "r", encoding="utf-8")

teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

pricelist = []
soitjad = []
for row in f:
    a = row.split(",")
    if a[2][-2:] == "\n":
        hind = float(a[1]) + teepikkus * float(a[2][2:])
    else:
        hind = float(a[1]) + teepikkus * float(a[2])
    soitjad.append(a[0])    
    pricelist.append(hind)

print("Kõige odavam on:", soitjad[pricelist.index(min(pricelist))])

f.close()

