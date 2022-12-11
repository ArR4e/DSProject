kasutajanimi = input("Sisestage kasutajanimi: ")

paroolyks = ""
paroolkaks = ""

while True:
    
    paroolyks = input("Sisestage parool: ")
    paroolkaks = input("Sisestage parool uuesti: ")
    
    if paroolyks == paroolkaks:
        
        if len(paroolyks) >= 8:
            
            if not paroolyks.isalpha():
                
                if not paroolyks.isnumeric():
                    
                    paroolyks = paroolyks[::-1]
                    
                    f = open("users.txt", "w")
                    f.write(kasutajanimi + ":" + paroolyks)
                    f.close()
                    
                    break
                
                else:
                    print("Sisestatud paroolis pole kasutatud tähti!")
                    
            else:
                print("Sisestatud paroolis pole kasutatud numbreid!")
                
        else:
            print("Sisestatud parool pole vähemalt 8 tähemärki pikk!")
            
    else:
        print("Sisestatud paroolid ei kattu!")