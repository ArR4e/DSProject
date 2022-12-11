# 1. Plokkskeem / RP

nimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")

    if parool1 != parool2:
        print("Paroolid ei kattu.")
        continue
    if len(parool1) < 8:
        print("Parool liiga lühike.")
        continue
    if parool1.isalpha() == True or parool1.isnumeric() == True:
        print("Pead kasutama nii tähti, kui ka numbreid.")
        continue
    
    break

parool = parool1 [::-1]

fail = open("users.txt", "a")
fail.write(nimi + ":" + parool + "\n")
fail.close()