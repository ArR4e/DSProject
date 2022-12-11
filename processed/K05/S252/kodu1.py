def sobivus():
    if len(parool)< 8:
        return "Parool peab olema vähemalt 8 tähemärki"
    elif not any(char.isdigit() for char in parool):
        return "Paroolis peab olema vähemalt üks number"
    else:
        return "OK"
    
kasutajanimi = input("Sisesta kasutajanimi:")
while True:
    parool = input("Sisesta parool:")
    parooluuesti = input("Sisesta parool uuesti:")
    if parooluuesti == parool:
        tulemus = sobivus()
        if tulemus == "OK":
            break
        else:
            print(tulemus)
    else:
        print("Paroolid ei kattu")

pooratud = (parool)
pooratudparool = "".join(reversed(pooratud))
print(pooratudparool)

pooratudk = (kasutajanimi)
pooratudkasutajanimi = "".join(reversed(pooratudk))
print(pooratudkasutajanimi)

f = open("users.txt","w")
f.write(pooratudkasutajanimi + pooratudparool)
f.close()