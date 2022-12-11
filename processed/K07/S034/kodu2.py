tee_pikkus_koju = float(input("Palun sisesta tee pikkus koju kilomeetrites: "))
f = open("taksohinnad.txt")
odavaim_hind = 0
odavaima_hinnaga_takso_nimi = ""
mitmes = 0

for rida in f:
        rida = (rida.strip()).split(",")
        takso_nimi = rida[0]
        sisseastumise_hind = float(rida[1])
        km_hind = float(rida[2])
        hind_kokku = sisseastumise_hind + tee_pikkus_koju * km_hind
        mitmes +=1
        if mitmes == 1:
            odavaim_hind = hind_kokku
            odavaima_hinnaga_takso_nimi = takso_nimi
        if hind_kokku < odavaim_hind:
            odavaim_hind = hind_kokku
            odavaima_hinnaga_takso_nimi = takso_nimi
if odavaim_hind != 0:
    print("Kõige odavam on", odavaima_hinnaga_takso_nimi)

f.close()