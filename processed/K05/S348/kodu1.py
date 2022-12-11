kasutajanimi = input("Sisestage enda kasutajanimi: ")
while True:
    parooltagurpidi = ""
    parool1 = input("Sisestage enda parool esimest korda: ")
    parool2 = input("Sisestage enda parool teist korda: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if parool1.isnumeric() == False and parool1.isalpha() == False:          
                parooltagurpidi = parool1[::-1]
                break
            else:
                print("Parool peab koosnema vähemalt ühest tähest ja numbrist")
        else:
            print("Paroolis peab olema vähemalt 8 tähemärki")
    else:
        print("Paroolid ei kattu")
        
fail = open("users.txt" , "w")
fail.write(kasutajanimi + ":")
fail.write(parooltagurpidi)
fail.close()


    
            
        
        
    
        
       
    