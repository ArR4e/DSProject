from math import pi

while True:


    nimi = str(input("Sisesta koogi nimetus: "))
    if nimi == "":
    
    
        break
    
    mõõt = float(input("Sisesta koogi mõõt: "))




    def koogi_hind(nimi, mõõt):
        if nimi == "ðokolaadikook":
        
            pindala = pi * mõõt **2
            return round(0.06*pindala, 2)

        elif nimi == "Napoleoni kook":
        
            pindala = mõõt **2
            return round(0.10*pindala, 2)
    
        elif nimi == "ploomikook":
        
            pindala = pi * mõõt **2
            return round(0.04*pindala, 2)
    
        
    
        else:
            raise ValueError("Sellist kooki andmebaasist ei leitud")
    
    print("Koogi hind on:",koogi_hind(nimi, mõõt), "eurot.")
    
    
        
        

        

        
    


    
    






