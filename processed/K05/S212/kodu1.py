def sobiv_parool(parool):
    character = False
    digit = False
    for char in parool:
        if char.isalpha():
            character = True
        if char.isdigit():
            digit = True
    if digit and character:
        return True
    else:
        return False
    
kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool = input("Parool: ")
    kordus = input("Korrake parooli: ")
    if not parool == kordus:
        print("Paroolid ei kattu.")
        continue
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemarki pikk.")
        continue
    elif not sobiv_parool(parool):
        print("Parool peab sisaldama nii tähti kui ka numbreid.")
        continue
    break

i = len(parool) - 1
cyphered = ""

while i >= 0:
    cyphered += parool[i]
    i -= 1
    
with open("users.txt","w") as f:
    f.write(kasutajanimi + ":" + cyphered)
    

