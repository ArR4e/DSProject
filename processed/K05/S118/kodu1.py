kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool esimest korda: ")
    parool2 = input("Sisestage parool teist korda: ")
    if parool1 != parool2:
        print("Esimene parool ei kattu teise parooliga.")
        continue
    elif len(parool1) < 8:
        print("Parool peab olema vähemalt 8 tähemärgi pikkune.")
        continue
    sisaldab_numbrit = False
    sisaldab_tähti = False
    for täht in parool1:
        if not täht.isalpha():
            sisaldab_numbrit = True
        else:
            sisaldab_tähti = True
    if sisaldab_numbrit and sisaldab_tähti:
        break
    else:
        print("Parool peab sisaldama nii tähti kui ka numbreid.")

fail = open("users.txt", "a")
fail.write("\n" + kasutajanimi + ":" + parool1[::-1])
fail.close()