nimi = input("Sisesta nimi: ")

encr = ''
while True:
    pw = input("Sisesta parool: ")
    pw2 = input("Sisesta parool uuseti: ")
    isal = False
    isnum = False
    if pw == pw2:
        if len(pw) >= 8:
            for i in pw:
                if i.isalpha():
                    isal = True
                if i.isnumeric():
                    isnum = True
            if isnum == isal:
                encr = pw[::-1]
                break
            else:
                print("Parool peab sisaldama nii numbreid kui ka tähti. Proovi uuesti.")
        else:
            print("Parool peab olema vähemalt 8 märki pikk. Proovi uuesti.")
    else:
        print("Paroolid ei ühti. Proovi uuesti. ")
f = open("users.txt", "w+")
f.write("{0}:{1}".format(nimi, encr))
f.close()
