kasutajanimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool teist korda: ")
    a = parool1.isalpha()
    b = parool1.isnumeric()
    c = len(parool1)
    if parool1 == parool2:
        if len(parool1) >= 8:
            if a != True and b != True:
                ümberpööratud = parool1[c::-1]
                fail = open("users.txt", "w")
                fail.write(kasutajanimi + ":" + ümberpööratud)
                fail.close()
                break
            else:
                print("Parool peab sisaldama tähti ja numbreid")
        else:
            print("Parool peab olema vähemalt 8 tähemärki pikk")
    else:
        print("Paroolid ei kattu, sisesta uuesti")