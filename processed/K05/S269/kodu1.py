import string
while True:
    user = input("kasutajanimi: ")
    pw = input("parool: ")
    pw2 = input("parool uuesti: ")
    if pw != pw2:
        print("Sisestatud paroolid ei kattu.")
        continue
    elif len(pw) < 8:
        print("Parool peab olema vähemalt 8 tähemärki pikk.")
        continue
    else:
        täht = 0
        nr = 0
        for i in range(len(pw)):
            if pw[i] in string.ascii_letters:
                täht = 1
            elif pw[i] in string.digits:
                nr = 1
        if täht and nr:
            break
        else:
            print("Paroolis peab olema kasutatud nii tähti kui numbreid.")
            continue
pw_r = pw[::-1]
f = open("users.txt", "w")
f.write(user + ":" + pw_r)
f.close()
