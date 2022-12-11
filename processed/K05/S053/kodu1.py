import re
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

kasutajanimi = str(input("Sisesta kasutajanimi: "))

while True:
    parool1 = str(input("Sisesta parool esimest korda: "))
    parool2 = str(input("Sisesta parool teist korda: "))
    while True:
        if parool1 == parool2:
            if len(parool2) >= 8:
                if re.search(str(number), parool2):
                    parool = parool2
                    pikkus = len(parool)
                    loorap = parool[pikkus: :-1]
                    f = open("users.txt", "w")
                    f.write(kasutajanimi + ':' + loorap)
                    f.close()
                else:
                    print("Sisesta parool uuesti!")
                    break
            else:
                print("Sisesta parool uuesti!")
                break
        else:
            print("Sisesta parool uuesti!")
            break

