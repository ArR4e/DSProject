while True:
    kasutajanimi = input("Sisesta kasutajanimi: ")
    parool_1 = input("Sisesta parool esimest korda: ")
    parool_2 = input("Sisesta parool teist korda: ")
    
    if parool_1 == parool_2:
        if len(parool_1) >= 8:
            if parool_1.isalpha and parool_1.isdigit:
                reversed = "".join(reversed(parool_1))
                f = open("users.txt", "w")
                f.write(kasutajanimi + ":")
                f.write(reversed)
                f.close()
                break
                
            else:
                print("Tekkis viga! Proovi uuesti!")
        else:
            print("Tekkis viga! Proovi uuesti!")
    else:
        print("Tekkis viga! Proovi uuesti!")


        
    

