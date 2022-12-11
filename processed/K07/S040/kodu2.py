pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
hinnad = []
nimed = []
if pikkus == 0:
    print("Taksot pole vaja")
else:
    fail = open("taksohinnad.txt", "r")
    for rida in fail:
        uus_rida = rida.split(",")
        nimi = uus_rida[0]
        sisseistumine = uus_rida[1]
        km_hind = uus_rida[2]
        hind = float(sisseistumine) + pikkus * float(km_hind)
        hinnad.append(hind)
        nimed.append(nimi)
    fail.close()
väikseim = min(hinnad)
indeks = hinnad.index(väikseim)

print("Kõige odavam on " + nimed[indeks])