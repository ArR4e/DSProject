s = float(input("Sisestage tee pikkus koju kilomeetrites: "))
fail = open("taksohinnad.txt", "r", encoding = "UTF-8")

odavaim = []
takso = []
try:
    for rida in fail:
        sisu = rida.strip("\n").split(",")
        hind = float(sisu[1]) + float(sisu[2]) * s
        odavaim += [hind]
        takso += [sisu[0]]

    min(odavaim)
    vastab = takso[odavaim.index(min(odavaim))]
    print("Kõige odavam on", vastab + ".")
except:
    print("Faili sisu on tühi.")

fail.close()