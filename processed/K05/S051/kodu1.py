kasutaja_nimi = input("Sisestage kasutajanimi: ")

while True:
    parool = input("Sisestage parool: ")
    parooli_kontroll = input("Sisestage parool uuesti: ")
    if parool != parooli_kontroll:
        print("Paroolid ei ühti. Proovige uuesti.")
        continue
    elif len(parool) < 8:
        print("Parool ei ole vähemalt 8 tähemärki pikk. Proovige uuesti.")
        continue
    elif parool.isalpha() or parool.isdigit():
        print("Paroolis pole kasutatud nii tähti kui ka numbreid. Proovige uuesti.")
        continue
    else:
        break

loorap = parool[::-1]

f = open("users.txt", "w")
f.write(kasutaja_nimi + ":" + loorap)
f.close()