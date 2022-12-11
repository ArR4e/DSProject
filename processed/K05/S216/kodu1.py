nimi = str(input("Sisesta kasutajanimi: "))

    
b = 0
u = 0
while True:
    parool1 = str(input("Sisesta parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))
    if parool2 != parool1:
        print("Paroolid ei kattu!")
        continue
    else:
        if len(parool1) < 8:
            print("Parool liiga lühike!")
            continue
         #kui tal pole nr sees siis tal kõik tähed
        else:
            if parool1.isalpha() == True:
                print("Pole piisavalt numbreid!")
                continue
            elif parool1.isnumeric() == True:
                print("Pole piisavalt tähti!")
                continue
            else:
                a = parool1[:: -1]
                f = open("users.txt", "w")
                
                f.write(str(nimi) + ":" + str(a))
                f.close()
                break
                
                
                    
        
