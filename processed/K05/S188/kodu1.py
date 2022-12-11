kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool esimest korda: ")
    parool2 = input("Sisesta parool teist korda: ")
    if parool1 != parool2:
        print("Paroolid ei tohi olla erinevad! Proovi uuesti!")
        continue
    if len(parool1) < 8:
        print("Parool peab olema vähemalt 8 tähemärki pikk! Proovi uuesti!")
        continue
    if parool1.isalpha() or parool1.isnumeric():
        print("Parool peab sisaldama nii tähti kui ka numbreid! Proovi uuesti!")
        continue
    break

i = len(parool1) - 1
krüpteeritud_parool = ""
while i >= 0:
    krüpteeritud_parool += parool1[i]
    i -= 1

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + krüpteeritud_parool)
f.close()