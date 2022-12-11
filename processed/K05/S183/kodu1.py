nimi = input("Sisesta kasutajanimi: ")

while True:
    parool_1 = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool teist korda: ")
    if parool_1 != parool_2:
        print("Esimene parool ei ühtinud teise parooliga, sisestage oma paroolida uuesti")
    elif len(parool_1) < 8:
        print("Parool on liiga lühike. Parool peab olema vähemalt 8 tähemärki")
    elif parool_1.isalpha() == False and parool_1.isnumeric() == False and parool_1.isalnum() == True:
        break
    elif parool_1.isalpha() == False and parool_1.isnumeric() == False and parool_1.isalnum() == False:
        x = False
        y = False
        for i in parool_1:
            if i.isalpha() == True:
                x = True
            if i.isnumeric() == True:
                y = True
        if x == True and y == True:
            break
    else:
        print("Parool peab sisaldama nii tähti kui ka numbreid")


parooli_pikkus = len(parool_1)
pööre = parool_1[parooli_pikkus::-1]
fail = open("users.txt", "w")
f = fail.write(nimi + ":" + pööre)
fail.close()