kasutajanimi = str(input("Sisesta oma kasutajanimi: "))

def main():
    
    parool = str(input("Sisesta oma parool: "))
    parool_confirm = str(input("Sisesta oma parool uuesti: "))

    def symbolid(parool):
        a = 0
        b = 0
        
        if parool == parool_confirm:
            pikkus = len(parool)
            if pikkus >= 8:
                
                for character in parool:
                    if character.isdigit():
                        a = 1
                    if character.isalpha():
                        b = 1
                if a == 0:
                    print("Parool ei sisalda numbreid. Sisesta palun uus parool.")
                    main()
                else:
                    if b == 0:
                        print("Parool ei sisalda tähti. Sisesta palun uus parool.")
                        main()
                    else:
                        parool_reversed = parool[::-1]
                        fail = open("users.txt", "w")
                        fail.write(kasutajanimi)
                        fail.write(":")
                        fail.write(parool_reversed)
                        fail.close()
                        
                    
            else:
                print("Parool on lühem kui 8 sümbolit. Sisesta palun uus parool.")
                main()
        else:
            print("Paroolid ei kattu. Sisesta palun uuesti.")
            main()
    
    symbolid(parool)
    

main()

    