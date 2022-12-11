nimi = input("Sisestage kasutajanimi: ")
while True:
    i = 0
    parool = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool != parool2:
        print("Sisestasite parooli valesti.")
        i += 1
    arv = len(parool)
    if arv < 11:
        if i < 1:
            print("Paroolis peab olema vähemalt 11 tähemärki.")
            i += 1
    if i < 1:
        tähed = parool.isalpha()
        numbrid = parool.isnumeric()
        if tähed or numbrid == False:
            break
        elif tähed and numbrid == True:
            print("Paroolis peab olema nii tähti, kui ka numbreid.")
    else:
        break
tagasi = parool[arv: :-1]
with open("users.txt", "w") as f:
    f.write(nimi + ":" + tagasi)
f.close