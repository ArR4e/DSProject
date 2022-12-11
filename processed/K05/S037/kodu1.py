kasutajanimi = input("Sisestage oma kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    
    if parool1 == parool2 and len(parool1) >= 8:
        number = 0
        täht = 0
        nimi = ""
        for sümbol in parool1:
            if sümbol.isdigit():
                number += 1
            else:
                täht += 1
        if number <= 0 or täht <= 0:
            print("Parool peab sisaldama nii tähti kui ka numbreid. Proovige uuesti!")
            parool1 = input("Sisestage parool: ")
            parool2 = input("Sisestage parool uuesti: ")
            continue
        else:
            def tagurpidi(parool1):
                nimi = "".join(reversed(parool1))
                return nimi
            fail = open('users.txt', 'w')
            f = (kasutajanimi + ":" + tagurpidi(parool1) + "\n")
            fail.writelines(f)
            fail.close()
            break

    else:
        print("Parooli sisestamisel on tekkinud viga. Proovige uuesti!")
        continue
