kasutajanimi = input("Sisesta soovitud kasutajanimi: ")
parool = input("Sisesta soovitud parool: ")
loorap = ""
while parool == input("Sisesta parool uuesti: "):
    if len(parool) > 7:
        if (str.isdigit(parool) == False) and (str.isalpha(parool) == False):
            for i in range(len(parool)):
                loorap =  loorap+(parool[-i-1])
        else:
            print("Parool peab sisaldama tähti ja numbreid!")
            parool = input("Sisesta uus parool: ")
            continue
    else:
        print("Parool peab olema vähemalt 8 tähemärki pikk!")
        parool = input("Sisesta uus parool: ")
        continue
    break

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + loorap)
f.close()