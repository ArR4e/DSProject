from math import pi

kook = input("Koogi nimi (sobivad 'šokolaadikook', 'ploomikook ja 'Napoleoni kook'): ")


while kook == "šokolaadikook" or kook =="ploomikook" or kook == "Napoleoni kook":
        
    mõõt = float(input("Koogi mõõt: "))
    
    def koogi_hind(kook, mõõt):
        
        if kook == "šokolaadikook":
           hind= mõõt ** 2 * pi * 0.06
        elif kook == "ploomikook":
            hind = mõõt ** 2 * pi * 0.04
        else:
            hind = mõõt * mõõt * 0.10
        return(round(hind, 2))
        
    print(koogi_hind(kook, mõõt))
        
    kook = input("Koogi nimi (sobivad 'šokolaadikook', 'ploomikook ja 'Napoleoni kook'): ")
        
    if kook == "":
        break
    
else:
    print("Sellist kooki andmebaasist ei leidu.")
        
        