import math

def koogi_hind(nimi, mõõdu):
        
    if nimi == "šokolaadikook":
        return round(((mõõdu**2 * math.pi) * 0.06), 2)
                            
    elif nimi == "ploomikook":
        return round(((mõõdu**2 * math.pi) * 0.04), 2)
                            
    elif nimi == "Napoleoni kook":
        return round(((mõõdu**2) * 0.10), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        
while True:
    name = input("Sisestage koogi nimi: ")
    size = float(input("Sisestage mõõdu: "))
    try:
        print(koogi_hind(name, size))
    except:
        print("Proovige uuesti...")
    else:
        break
