import math
śokolaadikook = 00.6 #euro/cm**2
ploomikook = 00.4
napoleoni_kook = 0.10

def koogi_hind(name_of_cake, size):
    if name_of_cake == "sokolaadikook":
        return round((math.pi * size ** 2) * śokolaadikook, 2)
    elif name_of_cake == "ploomikook":
        return round((math.pi * size ** 2) * ploomikook, 2)
    elif name_of_cake == "napoleoni kook":
        return round(size ** 2 * napoleoni_kook, 2)
    else:
        print("Sellist kooki andmebaasist ei leitud.")
        return None


print(f"Tervist! Meie praeguses asortimentis on kolm koogi varianti. Praegu kättesaadavat on sokolaadikook, ploomikook ja napoleoni kook!.")
print(f" Sokolaadikooki hind on {śokolaadikook} euro/cm^2, ploomikooki hind on {ploomikook} euro/cm^2, napoleoni hind on {napoleoni_kook}euro/cm^2.")


name_of_cakes = None
while True:
    name_of_cakes = input("Sisestage palun koogi nimi: ")
    if name_of_cakes == "":
        break
    sizes = input("Sisetage palun koogi mõõdu: ")
    
    
    try:
        sizes = float(sizes)
    except:
        print(f"Vale mõõdu ühikud.")
        continue
    m = koogi_hind(name_of_cakes, sizes)
    if m:
        print(f"{m} euro")
    
 
    
        
    

   

         
                                   
                                   