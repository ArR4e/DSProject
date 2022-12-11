kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool = input("Sisesta parool: ")
    parool_uuesti = input("Sisesta parool uuesti: ")
    if parool == parool_uuesti:
        if len(parool) >= 8:
            tähti = 0
            numbrid = 0
            for täht in parool:
                if tähti == 0 or numbrid == 0:
                    if täht.isalpha():
                        tähti += 1
                    elif täht.isnumeric():
                        numbrid += 1
                else:
                    break
            if tähti > 0 and numbrid > 0:
                break
            else:
                print("Parool ei sisaldanud nii numbreid kui ka tähti")
        else:
            print("Parool oli liiga lühike")
    else:
        print("Paroolid ei kattunud")

fail = open("users.txt", "w")
fail.write(kasutajanimi + ":" + parool[::-1])
fail.close()
