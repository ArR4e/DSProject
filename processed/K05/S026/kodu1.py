kasutaja = input("Palun sisesta kasutajanimi: ")
parool1 = input("Palun sisesta parool: ")
parool2 = input("Palun sisesta parool uuesti: ")


if parool1 != parool2:
    print("Sisestatud paroolid ei ole samad")
    katsed = 0
    while katsed < 2:
        parool1 = input("Palun sisesta parool: ")
        parool2 = input("Palun sisesta parool uuesti: ")
        katsed += 1
        print("Sisestatud paroolid ei ole samad")
        if parool1 == parool2:
            pass
    
elif len(parool1) < 8:
    print("Sisestatud parool ei ole piisavalt pikk")
    
elif not any(chr.isnumeric() for chr in parool1):
    print("Sisestatud paroolis peab olema vähemalt 1 täht või number")
    
else:
    suured = parool1.upper()
    if suured.isupper() == False:
        print("Sisestatud paroolis peab olema vähemalt 1 täht või number")
    
    parool = parool1 [::-1]
    f = open("users.txt", "a")
    f.write(kasutaja + ":" + parool + "\n")
    f.close()