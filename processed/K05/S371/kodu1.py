kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool veel kord: ")
    täht = 0
    number = 0

    if parool != parool_2:
        print("Esimene parool ei kattu teise parooliga. Proovi uuesti!")
    else:
        if len(parool) < 8:
            print("Parool peab olema vähemalt 8 tähemärki pikk. Proovi uuesti!")
        else:
            for i in parool:
                if i.isalpha():
                    täht = 1
                elif i.isdigit():
                    number = 1
            if täht + number == 2:
                parool = parool[::-1]
                fail = open("users.txt", "w", encoding = "UTF-8")
                fail.write(kasutajanimi + ":" + parool)
                fail.close()
                break
            else:
                print("Parool peab sisaldama nii tähti kui ka numbreid. Proovi uuesti!")
            
    
