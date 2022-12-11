kasutajanimi = input("Sisesta kasutajanimi: ")



while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")

    if str(parool1)!=str(parool2):
        print("Sisestatud parool ei ole sama")
        continue
    else:
        if len(str(parool1))<8:
            print("Parool pole piisavalt pikk")
            continue
        else:
            m = any(map(str.isdigit,parool1))
            if m == False:
                print("Parool ei sisalda numbrit")
                continue
            else:
                if parool1.isnumeric() == True:
                    print("Parool ei sisalda tähti")
                    continue
                else:
                    parool = str(parool1)[::-1]
                    f = open("users.txt","w+")
                    
                    f.write(str(kasutajanimi)+":"+str(parool))
                    f.close()
                    print("Programm lõpetatud")
                    break
