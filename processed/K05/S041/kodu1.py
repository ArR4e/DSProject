
kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
    if parool1 == parool2:
        if len(parool2) >= 8:
            if parool2.isalnum() == True:
                a = parool2 [::-1]
                f = open("users.txt", "r+")
                f.write(kasutajanimi + ":" + " " + a)
                f.close()
                
                print("Parool õige")
                #print(a)
                break
    
    else:
        print("Parool vale, proovi uuesti")
        
    
                

                
    
    


    
    
