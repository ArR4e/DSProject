nimi = input("Sisesta kasutajanimi: ")
while True:
    psw1 = input("Sisesta parool: ")
    psw2 = input("Sisesta parool: ")
    
    if psw1 != psw2:
        print("Paroolid ei kattu")
        continue
    elif len(psw1) < 8:
        print("Parool on liiga lühike")
        continue
    elif psw1.isalnum() == True and psw1.isalpha() == True or psw1.isdigit() == True:
        print("Parool peab sisaldama nii tähti kui ka numbreid")
        continue
    else:
        psw1 = psw1[::-1]
        f = open("users.txt", "w")
        f.write(nimi + ":" + psw1)
        f.close()
        break