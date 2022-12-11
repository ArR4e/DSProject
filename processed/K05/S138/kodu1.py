i = 0
while i <= 3:
    if i == 0:
        kasutajanimi = input("Sisestage kasutajanimi:")
        i = 1
    if i == 1:
        parool1 = input("Sisestage parool:")
        parool2 = input("Sisestage parool uuesti:")
        i = 2
    if i == 2:
        if parool1 != parool2:
            i = 1
            print("Paroolid ei kattu omavahel.")
        elif len(parool1) < 8:
            i = 1
            print("Parool peab sisaldama vähemalt 8 tähemärki.")
        else:
            if parool1.isnumeric() or parool1.isalpha():
                i = 1
                print("Parool peab sisaldama tähti ja numbreid.")
            else:
                i = 3
    if i == 3:
        l = len(parool1)
        tparool = parool1[l::-1]
        print(tparool)
        f = open("users.txt", "w+")
        sisend = [kasutajanimi+":"+tparool]
        f.writelines(sisend)
        f.close()
        i = 4
                
                