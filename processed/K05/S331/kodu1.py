kasutajanimi = input("Sisesta kasutajanimi:")
while True:
    parool = input("Sisesta parool:")
    parool2 = input("sisesta parool teist korda:")
    if parool == parool2:
        pikkus = len(parool)
        if pikkus >= 8:
            if parool.isalpha() or parool.isdigit():
                print("Sisestatud parool peab sisaldama nii numbreid kui ka tähti")
                continue
            else:
                parool_tagurpidi = parool[::-1]
                break
        else:
            print("Sisestatud parool peab olema vähemalt 8 tähemärki pikk")
            continue
    else:
        print("Sisestatud paroolid ei kattu")
        continue
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + parool_tagurpidi)
f.close()


        
        
        