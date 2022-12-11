from math import pi
def koogi_hind(kook,mõõde):

    if kook == "šokolaadikook":
        return round(0.06 * pi * mõõde**2 , 2)
    
    if kook == "ploomikook":
        return round(0.04 * pi * mõõde**2 , 2)
    
    if kook == "Napoleoni kook":
        return round(0.1 * mõõde**2 , 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")



while True:
    kook = input("Sisestage koogi nimi, kui rohkem ei soovi, vajutage enter: ")
    if kook == "":
        break
    mõõde = float(input("Sisestage koogi mõõde: "))

    print(koogi_hind(kook,mõõde))