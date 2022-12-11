kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if not parool1.isalpha() and not parool1.isdigit():
                tagurpidi = parool1[:: -1]
                f = open("users.txt", "w")
                f.write(kasutajanimi + ":" + tagurpidi)
                f.close()
                break
            else:
                print("Paroolis peavad olema nii numbrid kui ka tähed.")
        else:
            print("Paroolis peab olema vähemalt 8 tähemärki!")
    else:
        print("Paroolid ei kattu.")