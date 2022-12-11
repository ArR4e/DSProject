# Plokkskeem

nimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage esimene parool: ")
    parool2 = input("Sisestage teine parool: ")
    # 1. kontroll
    if parool2 != parool1:
        print("Teine parool ei ühti esimesega!")
        continue
    # 2. kontroll
    if len(parool2) < 8:
        print("Teie parool on lühem kui 8 tähemärki!")
        continue
    # 3. kontroll
    if parool2.isalpha() or parool2.isdecimal():
        print("Teie paroolis on ainult tähed või numbrid")
        continue
    else:
        break


viimane_parool = parool1[::-1]

f = open("users.txt", "w")
f.write(nimi + ":" + viimane_parool)
f.close()