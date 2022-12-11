def parool():
    parool1 = input("Sisesta oma parool: ")
    parool2 = input("Korda oma parool: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
                if any(str.isdigit(täht) for täht in parool1):
                    f = open('users.txt', 'w')
                    f.write(f"{kasutajanimi}:{parool1[::-1]}")
                else:
                    print('Peab kasutama nii tähti kui ka numbreid')
                    parool()
        else:
            print('Parool peab olema vähemalt 8 tähemärki')
            parool()
    else:
        print('Paroolid ei kattu')
        parool()
            
kasutajanimi = input("Sisesta kasutajanimi: ")
parool()