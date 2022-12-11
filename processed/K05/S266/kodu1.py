nimi = input("Sisestage oma kasutajanimi: ")

olek = "parool1"
while olek != "OK":
    if olek == "parool1":
        parool1 = input("Sisestage oma parool: ")
        olek = "parool2"
        continue
    if olek == "parool2":
        parool2 = input("Sisestage oma parool uuesti: ")
        if parool1 != parool2:
            print("Paroolid on erinevad.")
            olek = "parool1"
            continue
        if len(parool1) < 8:
            print("Sisestatud parool on liiga lühike.")
            olek = "parool1"
            continue
        taht = False
        for i in parool1:
            if i.isalpha():
                taht = True
                break
        if not taht:
            print("Parool peab sisaldama ka tähti.")
            olek = "parool1"
            continue
        number = False
        for i in parool1:
            if i.isnumeric():
                number = True
                break
        if not number:
            print("Parool peab sisaldama numbreid: ")
            olek = "parool1"
            continue
        olek = "OK"

tagurpidi = parool1[::-1]
fail = open("users.txt", 'w')
fail.write(nimi + ":" + tagurpidi)

fail.close()

               
                    
            
    