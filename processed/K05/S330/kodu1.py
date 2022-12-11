kasutajanimi = input("Sisestage kasutajanimi: ")
parool1 = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")

while True:
    if parool1 != parool2:
        print("Paroolid ei kattu!")
        parool1 = input("Sisestage parool: ")
        parool2 = input("Sisestage parool uuesti: ")
        continue
    elif len(parool1) < 8:
        print("Parooli pikkus peab olema vähemalt 8 tähemärki.")
        parool1 = input("Sisestage parool: ")
        parool2 = input("Sisestage parool uuesti: ")
        continue
    elif parool1.isdigit() or parool1.isalpha():
        print("Parool peab sisaldama nii tähti kui numbreid.")
        parool1 = input("Sisestage parool: ")
        parool2 = input("Sisestage parool uuesti: ")
        continue
    else:
        break
    
parool1 = parool1[::-1]

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + parool1)
f.close()       