kasutajanimi = input("Sisesta kasutajanimi: ")
parool1 = str(input("Sisesta parool: "))
parool2 = str(input("Sisesta parool uuesti: "))

if parool1 != parool2:
    print("Paroolid on erinevad.")
elif len(parool1) < 8:
    print("Parool peab olema vähemalt 8 tähemärki.")
elif any(chr.isdigit() for chr in parool1) == False:
    print("Parool peab sisaldama numbreid.")
elif any(chr.isalpha() for chr in parool1) == False:
    print("Parool peab sisaldama tähti.")
else:
    uus_parool = ""
    el = len(parool1)
    for i in range(len(parool1)):
        uus_parool += parool1[el-1]
        el -= 1
    fail = open("users.txt", "w")
    fail.write(str(kasutajanimi) + ":" + str(uus_parool))
    fail.close()
