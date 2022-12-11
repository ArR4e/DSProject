def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
nimi = str(input("Mis on teie kasutajanimi? "))
while True:
    parool1 = str(input("Sisestage oma parool: "))
    parool2 = str(input("Sisestage oma parool uuesti: "))
    if parool1 == parool2 and len(parool1) >= 8 and has_numbers(parool1):
        break
    else:
        print("Sisestamis oli viga. Proovige uuesti.")
paroolbackward = parool1[::-1]
f = open("users.txt", "w")
f.write(nimi + ":" + paroolbackward)
f.close()
