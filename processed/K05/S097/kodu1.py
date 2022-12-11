def parool():
    parool1 = input("Sisesta parool: ")
    parool2 = input("Korda parooli: ")
    
    if parool1 == parool2:
        sümbolite_arv = int(len(parool1))
        if sümbolite_arv >= 8:
            if parool1.isnumeric() == False:
                numbreid = 0
                i = 0
                while 0 <= i <= 9:
                    numbreid += parool1.count(str(i))
                    i += 1   
                if numbreid > 0:
                    a = parool1[::-1]
                    fail = open("users.txt", "w")
                    fail.write(kasutajanimi + ":" + a)
                    fail.close()
                else:
                    print("Parool peab sisaldama vähemalt ühte numbrit.")
                    parool()
            else:
                print("Parool ei tohi sisaldada ainult numbreid.")
                parool()
        else:
            print("Parool peab sisaldama vähemalt kaheksat tähemärki.")
    else:
        print("Paroolid ei kattu.")
        parool()
                            
  
kasutajanimi = input("Kasutajanimi: ")
parool()                       
        
