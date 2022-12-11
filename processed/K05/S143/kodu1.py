kasutajanimi = input("Sisesta kasutajanimi: ")
with open("users.txt", "a") as avatav_fail:
    while True:
        esimene_parool = input("Sisesta parool: ")
        teine_parool = input("Sisesta parool uuesti: ")
        tahe_ja_numbri_kontroll = []
        for tahemark in list(esimene_parool):
            try:
                s = int(tahemark)
                tahe_ja_numbri_kontroll.append(1)
            except:
                tahe_ja_numbri_kontroll.append(0)
        if esimene_parool != teine_parool:
            print("Paroolid ei ole samad!")
            continue
        elif len(esimene_parool) < 8:
            print("Parool on liiga lühike")
            continue
        elif 1 in tahe_ja_numbri_kontroll and 0 in tahe_ja_numbri_kontroll:
            avatav_fail.write(kasutajanimi + ":" + esimene_parool[::-1])
            break
        else:
            print("Parool peab sisaldama nii tähti kui ka numbreid")
            continue