knimi = input("Kasutajanimi: ")


while True:
    parool1 = input("Parool: ")
    parool2 = input("Parool uuesti: ")
    if parool1 != parool2:
        print("Paroolid ei kattu, proovi uuesti:")
    else:
        parool = parool2
        if len(parool) < 8:
            print("Parool on liiga lühike. Peab olema enam, kui 8 tähemärki.")
        else:
            sumarv = 0
            sumtaht = 0
            for m2rk in parool:
                if m2rk.isdecimal() == True:
                    sumarv += 1
                if m2rk.isalpha() == True:
                    sumtaht += 1
            if sumarv == 0 or sumtaht == 0:
                print("Parool peab sisaldama vähemalt ühte numbrit ja vähemalt ühte tähte.")
            tagurpidi = ""
            a  = -1
            for i in parool:
                uusm2rk = parool[a]
                a -= 1
                tagurpidi += uusm2rk
            with open("users.txt", "w") as f:
                f.write(knimi + ":" + tagurpidi)
            
            
            break