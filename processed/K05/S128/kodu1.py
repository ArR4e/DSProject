#Plokkskeem
from string import *
kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool = input("Sisesta parool: ")
    parool_kordus = input("Sisesta uuesti parool: ")
    if parool == parool_kordus:
        if len(parool) >= 8:
            if parool.isalpha() or parool.isdigit() == True:
                print("Paroolis peab leiduma nii tähti kui ka numbreid.")
            else:
                break
        else:
            print("Parool liiga lühike.")
    else:
        print("Paroolid ei kattu.")

parool_krüptitud = parool[::-1]

fail = open("users.txt", "w")
fail.write(kasutajanimi + ":")
fail.write(parool_krüptitud)
fail.close()

