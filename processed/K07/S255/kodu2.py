kaugus = float(input("Sisesta tee pikkus kilomeetrites: "))
odavaim = 1000000
try:
    with open("taksohinnad.txt", "r", encoding="UTF8") as ava_fail:
        for i in ava_fail:
            i = (i.strip()).split(",")
            nimi, algustasu, km_hind = i[0], float(i[1]), float(i[2])
            takso_tasu = algustasu + kaugus * km_hind
            if (takso_tasu) < odavaim:
                odavaima_nimi = nimi
                odavaim = takso_tasu
        print(f"Kõige odavam on {odavaima_nimi}")
except:
    print("Vigane fail")