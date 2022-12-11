f = open("taksohinnad.txt", "r", encoding = "utf-8")
tee_km = float(input("Tee pikkus koju kilomeetrites: "))
odavaim_hind = 1e10
odavaim_takso = "Kõik taksod on liiga kallid"

for rida in f:
    liik = "firma"
    nimi = ""
    algus_hind = ""
    km_hind = ""
    for täht in rida:
        if liik == "firma":
            if täht == ",":
                liik = "algus_hind"
                continue
            else:
                nimi += täht
        if liik == "algus_hind":
            if täht == ",":
                liik = "km_hind"
                continue
            else:
                algus_hind += täht
        if liik == "km_hind":
            if täht == "\n":
                continue
            km_hind += täht
    km_hind_nr = float(km_hind)
    algus_hind_nr = float(algus_hind)
    hind_kokku = algus_hind_nr + km_hind_nr * tee_km
    if hind_kokku < odavaim_hind:
        odavaim_takso = nimi
        odavaim_hind = hind_kokku
print("Kõige odavam on " + odavaim_takso)
            