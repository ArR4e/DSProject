kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool_1 = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool uuesti: ")
    if parool_1 == parool_2:
        parooli_pikkus = len(parool_1)
        if parooli_pikkus >= 8:
            ainult_tähed = str(parool_1.isalpha())
            ainult_numbrid = str(parool_1.isnumeric())
            if ainult_tähed == "False" and ainult_numbrid == "False":
                print("Kasutajanimi ja parool on salvestatud faili users.txt!")
                break
            else:
                print("Parool peab sisaldama nii numbreid kui ka tähti. Palun sisesta paroolid uuesti!")
        else:
            print("Parooli pikkus peab olema vähemalt 8 tähemärki. Palun sisesta paroolid uuesti!")
    else:
        print("Paroolid ei kattu. Palun sisesta paroolid uuesti!")
        

tagurpidi_parool = parool_1[::-1]
kasutajanimi_ja_parool = kasutajanimi + ":" + tagurpidi_parool

fail = open("users.txt", "w")
fail.write(kasutajanimi_ja_parool)
fail.close()