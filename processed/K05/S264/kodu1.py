kasutajanimi = input("Sisestage kasutajanimi: ")
parool1 = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")

def parool(sõne):
    if parool1 == parool2:
        return parool1
    else:
        print("Paroolid ei kattu!")
    if len(parool1) >= 8:
        return parool1
    else:
        print("Parool peab olema vähemalt 8 tähemärki pikk.")
    if 'parool1'.isalum() == False:
        return parool1
    else:
        print("Parool peab sisaldama nii tähemärke kui numbreid.")
    return parool

f = open("users.txt", "a")
f.write("Kasutajanimi:" + kasutajanimi + "\n" )
f.write("Parool:" + parool(parool1[::-1]))