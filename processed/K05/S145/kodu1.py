nimi = input("Sisestage kasutajanimi: ")

def parool():
    parool1 = input("Sisestage parool: ")
    parool2 = input("Kinnitage parool: ")
    if parool1 != parool2:
        print("Paroolid ei kattu")
        parool()
    else:
        if len(parool1) < 8:
            print("Parool on liiga lühike. Parool peab olema vähemalt 8 tähemärki pikk.")
            parool()
        else:
            if parool1.isalpha() == True:
                print("Parool peab sisaldama vähemalt ühte numbrit.")
                parool()
            elif parool1.isnumeric() == True:
                print("Parool peab sisaldama vähemalt ühte tähte.")
                parool()
            else:
                krypto = parool1[::-1]
                with open('users.txt', 'w') as u:
                    u.write(nimi + ":" + krypto)
parool()