f = open("users.txt", "w")
kasutajanimi = input("Sisesta kasutajanimi: ")
i = 0
parool = input("Sisesta parool: ")
while parool is not int:
    if len(parool) >= 8 and i < 3:
            parool_kordus = input("Sisesta parool uuesti: ")
            if parool == parool_kordus:
                print("OK")
                parool = parool [::-1]
                f.write(kasutajanimi+parool)
                f.close()
                break
            else:
                print("Paroolid ei kattu ")
                i += 1
    else:
        print("Parooli pikkus peab olema vähemalt 8 tähemärki \nParool peab sisaldama nii numbreid, kui tähti ")
        parool = input("Sisesta uus parool: ")
        i=0
        
