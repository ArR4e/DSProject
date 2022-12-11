import re
kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")
    if not parool1 == parool2:
        print("Paroolid ei kattu.")
        continue
    else:
        if len(parool1) <8:
            print("Parool on liiga lühike.")
            continue
        else:
            if not re.search("[0-9]", parool1):
                print("Parool peab sisaldama numbreid.")
                continue
            else:
                if not re.search("[a-z]", parool1):
                    print("Parool peab sisaldama tähti.")
                    continue
                else:
                    break
tagurpidi = parool1[::-1]
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + tagurpidi)
f.close()
                    