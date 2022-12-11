kasutajanimi = str(input("Kasutajanimi: "))

while True:
    parool = str(input("Parool: "))
    parool2 = str(input("Parool uuesti: "))
    if parool != parool2:
        print("Sisestatud paroolid ei kattu!")
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki!")
    elif parool.isdigit() == True:
        print("Parool peab sisaldama tähti!")
    elif parool.isalpha() == True:
        print("Parool peab sisaldama numbreid!")
    else:
        break

parool = parool[len(parool)::-1]

f = open("users.txt", "w")

f.write(str(kasutajanimi) + ":" + str(parool))

f.close()