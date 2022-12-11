
nimi = input("Sisesta kasutajanimi: ")

while True:
    parool = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    if parool2 != parool:
        print("Paroolid on erinevad!")
        continue
    elif len(parool) < 8:
        print("Parool on liiga lühike!")
        continue
    elif parool.isalpha() or parool.isnumeric() == True:
        print("Parool peab sisaldama tähti ja numbreid!")
        continue
    break

loorap = "".join(list(reversed(parool)))

fail = open("users.txt", "w")
sisu = "".join(["kasutajanimi: ", str(nimi) + "\n", "parool: ", str(loorap)])
fail.write(str(sisu))
fail.close()