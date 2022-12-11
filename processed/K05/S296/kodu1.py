kasutajanimi = input("Sisesta kasutajanimi:")



while True:
    parool1 = input("Sisesta parool:")
    parool2 = input("Sisesta parool uuesti:")
    if parool1 != parool2:
        print("Paroolid ei kattu, proovi uuesti.")
        continue
    if len(parool1) < 8:
        print("Parool on liiga lühike, proovi uuesti.")
        continue
    if parool1.isalpha() == True or parool1.isdigit == True:
        print("Parool peab sisaldama vähemalt ühte tähte ja ühte numbrit")
        continue
    f = open('users.txt','a')
    f.write(str(kasutajanimi)+":"+''.join(reversed(parool1)))
    f.close()
    break
    
                
                
                
                    