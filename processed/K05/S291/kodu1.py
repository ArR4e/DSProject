kasutajanimi = input("Palun sisesta kasutajanimi: ")

while True:
    parool = input("Palun sisesta parool: ")
    parooli_kinnitus = input("Palun sisesta parool veel üks kord: ")

    if parool == parooli_kinnitus:
        if len(parool) >= 8:
            if parool.isalpha() == False and parool.isnumeric() == False:
                tagurpidi_parool = parool[len(parool):: -1]
                fail = open("users.txt", "a")
                fail.write(kasutajanimi + ":" + str(tagurpidi_parool) + "\n")
                break
            else:
                print("Parool peab sisaldama tähti ja numbreid. Proovi uuesti!")
                continue
        else:
            print("Parool on liiga lühike. Proovi uuesti!")
            continue
    else:
        print("Esimene parool ei kattu teise parooliga. Proovi uuesti!")
        continue

fail.close()
            