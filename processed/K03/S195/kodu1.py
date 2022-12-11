
aastatulu = float(input("Palun sisestage oma aasta tulu: "))

if aastatulu > 0 and aastatulu < 6000 :
    
        maksuvaba = aastatulu
    
elif aastatulu >= 6000 and aastatulu < 14400 :
    
        maksuvaba = 6000
    
elif aastatulu >= 14400 and aastatulu < 25200 :
    
        maksuvaba = 6000-6000/10800*(aastatulu - 14400)
    
elif aastatulu >= 25200 :
    
        maksuvaba = 0
    
else :
        print("Aastatulu peab olema number, mis on 0 suurem.")
        exit()
        
        
maksuvaba = round(maksuvaba, 2)
print("Maksuvaba tulu on ", + maksuvaba,"eurot.")
        
        
                  