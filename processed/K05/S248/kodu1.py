nimi=input("Sisesta kasutajanimi: ")

while True:
    parool=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool!=parool2:
        print ("Paroolid ei kattu.")
        continue
    else:
        if len(parool)<8:
            print ("Parool liiga lühike")
        else:
            if parool.isalpha() == True or parool.isdigit() == True:
                print ("Parool peab sisaldama nii tähti kui numbreid.")
                continue
            else:
                parool=parool[::-1]
                f=open("users.txt", "w")
                f.write(nimi +":"+ parool)
                f.close()
                break

                

            
            
            
        