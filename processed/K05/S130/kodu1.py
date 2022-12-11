kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    paroola = input("Sisestage parool: ")
    paroolb = input("Sisestage parool uuesti: ")
    if paroola == paroolb:
        if len(paroola) >= 8:
            if paroola.isalpha():
                print("Parool peab sisestama v2hemalt yhte numbrit")
            else:
                if paroola.isnumeric():
                    print("Parool peab sisestama v2hemalt yhte t2hem2rki")
                else:
                    print("Parool sobib")
                    break
        else:
            print("Parool liiga lühike, peab olema vähemalt 8 tähemärki")
    else:
        print("Sisestatud paroolid ei ühti.")
    
paroolc = paroola[::-1]

f = open("users.txt", "x")
f.write(kasutajanimi + ":" + paroolc)
f.close()

    



