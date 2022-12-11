nimi = input("Sisesta kasutajanimi: ")
parool = input("Sisesta parool: ")
parool2 = input("Sisesta parool uuesti: ")
def sisaldab(parool):
    return not parool.isalpha() and not parool.isdigit()
while True:
    if parool == parool2 and len(str(parool)) > 7 and sisaldab(parool) == True:
        parool = parool[::-1]
        file = open("users.txt", "w")
        file.write(nimi + ":" + parool)
        file.close()
        break
    elif parool != parool2:
        print("Sisestatud paroolid on erinevad.")
    elif len(str(parool)) < 8:
        print("Parool peab olema 8 märgi pikkune.")
    elif sisaldab(parool) == False:
        print("Parool peab sisaldama numbreid ja tähti.")
    parool = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")