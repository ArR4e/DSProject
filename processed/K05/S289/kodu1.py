kasutajanimi = str(input("Sisesta oma kasutajanimi: "))
parool_1 = str(input("Sisesta oma parool: "))
parool_2 = str(input("Korda parooli: "))
if parool_1 == parool_2:
    if len(parool_1) >= 8:
        if parool_1.isalpha() == False and parool_1.isnumeric() == False:
            parool = parool_1[::-1]
            fail = open("users.txt", "w")
            fail.write(kasutajanimi + ":" + parool)
            fail.close()
        else:
            print("Kasutajaga esines puudusi")
    else:
        print("Kasutajaga esines puudusi")
else:
    print("Kasutajaga esines puudusi")
    

    