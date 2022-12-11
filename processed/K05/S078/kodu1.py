nimi = str(input("Sisestage kasutaja nimi: "))
while True:
    parool_1 = str(input("Sisestage parool: "))
    parool_2 = str(input("Sisestage parool veel üks kord: "))
    if parool_1==parool_2:
        if len(parool_2) >= 8:
            if parool_2.isalnum() == True:
                f = open("user.txt", "w")
                f.write(nimi + ":" + parool_2)
                f.close()
                break
            else:
                break
        else:
            continue
            print("Midage läks valesti")
    else:
        continue
    nimi = str(input("Sisestage kasutaja nimi: "))
while True:
    parool_1 = str(input("Sisestage parool: "))
    parool_2 = str(input("Sisestage parool veel üks kord: "))
    if parool_1==parool_2:
        if len(parool_2) >= 8:
            if parool_2.isalnum() == True:
                f = open("user.txt", "w")
                f.write(nimi + ":" + parool_2)
                f.close()
                break
            else:
                print("Parool siseldab keelatud sümbolid")
                continue
        else:
            print("On vaja vähemalt 8 tähemarki")
            continue
    else:
        print("Paroolid on erinevad")
        continue
