def viga():
    print("Ilmnes viga, proovi uuesti!")

def kontroll(parool1):
    if parool1.isalpha() == True and parool1.isnumeric() == True:
        return False
    else:
        return True
    
def pooramine(parool1):
    return parool1[::-1]

def kirjutamine(nimi,parool):
    f = open("users.txt", "w+")
    f.write(f"{nimi}:{parool}")
    f.close()

nimi = input("Sisestage soovitud kasutajanimi: ")
while True:
    parool1 = input("Sisestage soovitud parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if kontroll(parool1) == True:
                parool = pooramine(parool1)
                kirjutamine(nimi,parool)
                break
            else:
                viga()
        else:
            viga()
    else:
        viga()
        