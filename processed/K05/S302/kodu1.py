while True:
    kasutaja = input("Sisestage kasutajanimi: ")
    parool = input("Sisestage parool: ")
    parool2 = input("Sisestage parool teist korda: ")
    if parool == parool2:
        if len(parool) >= 8:
            if any(char.isdigit() for char in parool):
                uus = parool[::-1]
                fail = open("users.txt", "a")
                fail.write(kasutaja + ":" + uus + "\n")
                fail.close()
                break
            else:
                print("Paroolis peab olema nii numbrid kui ka tähed")
        else:
            print("Parool peab olema vähemalt 8 tähemärki pikk")
    else:
        print("Paroolid ei ühildu")