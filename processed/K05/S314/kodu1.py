kasutaja = input("Sisesta kasutajanimi: ")
while True:
    parool = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    if parool != parool2:
        print("Paroolid ei kattu!")
    else:
        if len(parool) < 8:
            print("Parool on liiga lühike!")
        else:
            if parool.isalpha() or parool.isnumeric():
                print("Parool peab sisaldama nii tähti kui numbreid!")
            else:
                break

f = open("users.txt", "w")
f.write(kasutaja + ":" + parool[::-1])
f.close()
# print(kasutaja + ":" + parool[::-1])

            