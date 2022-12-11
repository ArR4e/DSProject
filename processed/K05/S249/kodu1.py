kasutajanimi = str(input("Sisestage kasutajanimi: "))
parool = str((input("Sisestage parool: ")))
parool2 = str((input("Sisestage parool uuesti: ")))    


if parool != parool2:
    print("Paroolid on erinevad! ")
elif len(parool) < 8:
    print("Parool peab olema vähemalt 8 elementi pikk! ")
elif not(parool.isalnum()) and not(parool.isalpha()) and not(parool.isdigit):
    print("Parool peab sisaldama tähti ja numbreid! ")
else:
    uparool = ""
    e1 = len(parool)
    for i in range(len(parool)):
        uparool += parool[e1-1]
        e1 -= 1
    fail = open("users.txt", "w")
    fail.write(str(kasutajanimi) + ":" + str(uparool))
    fail.close()