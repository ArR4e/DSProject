kasutajanimi = input("Sisesta kasutajanimi: ").strip()
parool = input("Sisesta parool: ").strip()
parool2 = input("Sisesta teist korda parool: ").strip()

while True:
    if parool == parool2:
        if len(parool) == 8 or len(parool) > 8:
            if parool.isalnum():
                (parool[::-1])
                break
            else:
                print("Parooli ei sisalda endas nii numbreid kui ka tähti. Seega proovime uuesti.")
                parool = input("Sisesta parool: ").strip()
                parool2 = input("Sisesta teist korda parool: ").strip()
                continue
        else:
            print("Par2ooli pikkus peab olema vähemalt 8 tähemärki pikk. Seega proovime uuesti.")
            parool = input("Sisesta parool: ").strip()
            parool2 = input("Sisesta teist korda parool: ").strip()
            continue
    else:
        print("Esimene parool ei kattu teise parooliga. Seega proovime uuesti.")
        parool = input("Sisesta parool: ").strip()
        parool2 = input("Sisesta teist korda parool: ").strip()
        continue

rida = (kasutajanimi + ":" + (parool[::-1]))

f = open("users.txt", "w+")
f.write(rida)
f.close()
        
           
    
        