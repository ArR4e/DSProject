kasutajanimi=input("Kirjuta kasutajanimi:")
while True:
    parool_1=input("Kirjuta parool")
    parool_2=str(input("Kirjuta parool uuesti"))
    if parool_1==parool_2:
        pikkus=len(parool_1)
        if pikkus>=8:
           
            a=any(map(str.isdigit,parool_1))
            if a==True:
                parool=(parool_1[::-1])
                fail = open("users.txt", mode="w")
                fail.write(kasutajanimi + ":"+ parool+"\n")
                fail.close()
                break 
            else:
                print("Paroolis pole numbreid")
                break
        else:
            print("Paroolis pole kaheksat tähe märki.")
            break
    else:
        print("Paroolid ei kattu.")
        break
            