nimi = input("Palun sisestage oma kasutajanimi: ")

def arvjatäht(string): # Kontrollib kas sõnes on vähemalt 1 arv ja 1 täht - väljastab True kui on
    arv = False
    täht = False

    for sümbol in string:
        try:
            int(sümbol)
        except:
            sümbol = sümbol.lower()
            if sümbol.islower() == True:
                täht = True
        else:    
            arv = True
            
        finally:
            if täht == True and arv == True:
                return True
                break



while True:
    parool = input("Palun sisestage oma kasutaja parool: ")
    parool2 = input("Palun sisestage oma kasutaja parool: ")
    
    # Kontrollin kas parool on sama
    if parool != parool2:
        print("Teie paroolid ei olnud samasugused, proovige uuesti!")
        continue
    
    # Kontrollin kas parool on piisavalt pikk
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki pikk!")
        continue
    
    # Kontrollin kas paroolis on tähed ja numbrid
    elif arvjatäht(parool) != True:
        continue
        
        
   # Kui kõik tingimused läbitud tulen tsüklist välja
    break
   
# "krüpteerin parooli"        
uus_parool = []
parool = list(parool)
for i in range(len(parool)):
    uus_parool.insert(len(parool) -1 , parool[(i * -1) - 1])   
uus_parool = "".join(uus_parool)



# kirjutan kasutajanime ja parooli faili "users.txt" 
f = open("users.txt", "w")
f.write(nimi + ":" + uus_parool)
       
f.close()
