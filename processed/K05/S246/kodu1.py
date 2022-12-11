def number_ja_täht(parool):
    for x in parool:
        if x.isdigit():
            return True
    return False

while True:
    kasutajanimi = str(input("Sisesta kasutajanimi: "))
    parool = str(input("Sisesta parool: "))
    parooli_kontroll = str(input("Sisesta parool uuesti: "))
    if parool == parooli_kontroll:
        if len(parool) >= 8:
            if number_ja_täht(parool):
                parool_tagurpidi = parool[::-1]
                fail = open("users.txt", "w")
                fail.write(kasutajanimi + ":" + parool_tagurpidi + "\n")
                fail.close()
                break
            else:
                print("Kasuta numbreid ja tähti.")
        else:
            print("Kasuta vähemalt 8 tähemärki.")
    else:
        print("Paroolid ei kattu.")