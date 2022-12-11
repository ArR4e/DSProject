kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool_1 = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool veel üks kord: ")

    if parool_1 == parool_2:
        parool = parool_1 = parool_2
        tähed = 0
        numbrid = 0
        sümbolid = 0
        for i in parool:
            if i.isdigit():
                numbrid = numbrid + 1
            elif i.isalpha():
                tähed = tähed + 1
            else:
                sümbolid = sümbolid + 1
            parooli_pikkus = tähed + numbrid + sümbolid
        
        if parooli_pikkus < 8:
            print("Parool peab sisaldama vähemalt 8 tähemärki.")
            print("Proovi uuesti.")
            continue
        elif tähed == 0 or numbrid == 0:
            print("Parool peab sisaldama nii tähti kui numbreid.")
            print("Proovi uuesti.")
            continue
        else:
            break
    else:
        print("Paroolid ei kattu.")
        print("Proovi uuesti.")

parool_tagurpidi = parool[::-1]
fail = open("users.txt", "w")
tekst = (kasutajanimi + ":" + parool_tagurpidi)
fail.write(tekst)

fail.close()