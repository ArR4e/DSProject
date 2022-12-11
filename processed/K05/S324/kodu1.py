kasutajanimi = input("Palun sisesta kasutajanimi: ")

while True:

    parool_1 = input("Palun sisesta parool: ")
    parool_2 = input("Palun korda parooli: ")

    if parool_1 == parool_2:
        parooli_pikkus = len(parool_1)
    else:
        print("Paroolid ei kattu!")
        continue
    if parooli_pikkus >= 8:
        on_number = any(chr.isdigit() for chr in parool_1)
    else:
        print("Parool pole piisavalt pikk!")
        continue
    if on_number == True:
        on_täht = any(chr.isalpha() for chr in parool_1)
    else:
        print("Parool ei sisalda numbreid!")
        continue
    if on_täht == True:
        break
    else:
        print("Parool ei sisalda tähti!")
        continue

keeratud_parool = parool_1[:: -1]

fail = open("users.txt", "w")
fail.write(kasutajanimi + ":" + keeratud_parool)
fail.close()


        
        
        
        
            
    
        
              
    


