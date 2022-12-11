
nimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Parool uuesti: ")
    if parool1  == parool2:
        if len(parool1) >= 8:
            if not parool1.isalpha() and not parool1.isdigit():
                break
    print("Sisestatud paroolid ei sobi. Proovi uuesti!")
parool = parool1[::-1]
with open("users.txt", "w") as f:
    f.write(nimi + ":" + parool)
