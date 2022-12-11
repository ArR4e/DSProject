def checkstring(parool1):
    flag_1 = False
    flag_n = False
    for i in parool1:
        if i.isalpha():
            flag_1 = True
        if i.isdigit():
            flag_n = True
    return flag_1 and flag_n


kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Palun sisesta parool: ")
    parool2 = input("Palun korda parooli: ")
    if parool1 != parool2:
        print("Paroolid ei kattu, proovime uuesti.")
    else:
        if len(parool1) < 8:
            print("Parool on liiga lühike, peab sisaldama vähemalt 8 tähemärki. Proovime uuesti.")
        else:
             parool12 = checkstring(parool1)
             if parool12 is True:
                 parool = parool1[::-1]
                 f = open("users.txt", "w")
                 f.write(kasutajanimi + ":" + parool)
                 f.close()   
                 break
             else:
                print("Parool peab sisaldama nii numbreid kui ka tähti. Proovime uuesti.")               
