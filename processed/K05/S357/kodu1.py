kasutajanimi = input("Sisesta kasutajanimi: ")

def containsdigit(string):
    return any(char.isdigit() for char in string)

def containschar(string):
    return any(char.isalpha() for char in string)

def pööratud(string):
    return string[:: -1]

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
    if not(parool1 == parool2):
        print("Paroolid ei ühti!")
        continue
    if not(len(parool1) >= 8):
        print("Parool peab olema vähemalt 8 tähemärki!")
        continue
    if not(containsdigit(parool1) and containschar(parool1)):
        print("Parool peab sisaldama tähti ja numbreid!")
        continue
    break

fail = open("users.txt", "w")
fail.write((kasutajanimi + ":" + pööratud(parool1)))
fail.close()