nimi = input("Sisetage kasutajanimi: ")

while True:
    parool1 = input("Siestage parool: ")
    parool2 = input("Kinnitage oma parool: ")
    
    if parool1 != parool2:
        print("Paroolid ei kattunud. Sisestage uuesti.")
        continue
    elif len(parool1) < 8:
        print("Parool on liiga lühike. Sisestage uuesti.")
        continue
    elif parool1.isalpha() == True or parool1.isnumeric() == True:
        print("Parool peab sisaldama nii numbreid kui ka tähti")
        continue
    else:
        tagurpidi_parool = str(parool1)[::-1]
        break

fail = open("users.txt", "w")
fail.write(nimi + ":" + tagurpidi_parool)
fail.close()