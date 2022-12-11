teepikkus = float(input("Kodutee pikkus meetrites: "))
fail = open("taksohinnad.txt", encoding = "UTF-8")
stardihinnad = []
nimed = []
kilomeetrihinnad = []
teekonna_hinnad = []
for rida in fail:
    taksod = rida.split(",")
    stardihind = taksod[1]
    takso_nimi = taksod[0]
    kilomeetrid = taksod[2]
    kilomeetrid_2 = kilomeetrid.strip()
    stardihinnad.append(stardihind)
    nimed.append(takso_nimi)
    kilomeetrihinnad.append(kilomeetrid_2)
    hind_kokku = float(stardihind) + float(kilomeetrid)*teepikkus
    teekonna_hinnad.append(hind_kokku)

väikseim = min(teekonna_hinnad)
indeks = teekonna_hinnad.index(väikseim)

nimi = nimed[indeks]
print("Kõige odavam on " + nimi)

fail.close()
