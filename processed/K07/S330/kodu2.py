from math import inf
pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
a = inf
odavaim = "jalgsi"
f = open("taksohinnad.txt", encoding = "UTF-8")
for rida in f:
    if rida == "":
        break
    jupid = rida.strip()
    jupid = jupid.split(",")
    nimi = jupid[0]
    hind1 = float(jupid[1])
    hind2 = float(jupid[2])
    hind = hind1 + pikkus * hind2
    if hind < a:
        a = hind
        odavaim = nimi

print("Kõige odavam on " + str(odavaim) + ".")
f.close()