kasutajanimi = str(input("kasutajanimi: "))

while True:
    parool_1 = str(input("parool esimest korda: "))
    parool_2 = str(input("parool teist korda: "))
    x = parool_1.isalpha()
    y = parool_1.isnumeric()
    z = parool_1.isalnum()

    if parool_1 == parool_2:
        if len(parool_1) >= 8:
            if x== False:
                if y == False:
                    uus_parool = parool_1[::-1]
                    break
                else:
                    print("ära kasuta ainult numbreid")
            else:
                print("ära kasuta ainult tähti")
        else:
            print("parool liiga lühike")
    else:
        print("paroolid ei klapi")

fail=(open("users.txt", "w"))
fail.write(kasutajanimi + ":" + uus_parool)
fail.close()
        