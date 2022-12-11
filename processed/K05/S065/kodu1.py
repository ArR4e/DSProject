# 1. Plokkskeem (5. kodutöö)

Kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Korrake parooli: ")
    täht = 0
    number = 0
    
    if parool1 != parool2:
        print("Paroolid ei kattu. Proovige uuesti!")
    else:
        if len(parool1) < 8:
            print("Parool peab olema vähemalt 8 tähemärki.")
        else:
            for i in parool1:
                if i.isalpha():
                    täht = 1
                elif i.isdigit():
                    number = 1
                if täht + number == 2:
                    parool1 = parool1[::-1]
                    fail = open("users.txt", "w")
                    fail.write(Kasutajanimi + ":" + parool1)
                    fail.close()
                    break
                else:
                    print("Parool peab sisaldama nii numbreid kui ka tähti.")