import re
kasutajanimi = input("Sisesta kasutajanimi:")
while True:
    parool1 = input("Sisesta parool:")
    parool2 = input("Sisesta parool uuesti:")
    if parool1 != parool2:
        print("Paroolid ei kattu")
    elif len(parool2) < 8:
        print("Parool ei ole 8 tähemärki pikk.")
    elif not re.search("[0-9]", parool2):
        print("Paroolis peab olema vähemalt üks number")
    else:
        break
uus = "".join(reversed(parool2))

f = open("users.txt", "w")
f.write(kasutajanimi +":"+ uus)
f.close()