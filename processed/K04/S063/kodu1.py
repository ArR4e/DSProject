def koogi_hind(nimi, moot = 1):
    
    if (nimi == "šokolaadikook"):
         yhiku_hind = 0.06
    elif(nimi == "ploomikook"):
        yhiku_hind = 0.04
    elif (nimi == "Napoleoni kook"):
        yhiku_hind = 0.10
    else:
        print("\nSellist kooki ei leidu.\n")
        return False
    
    hind = round(float(moot)*yhiku_hind, 2)
    return hind
        

nimi, moot = "", ""

while nimi == "" or moot == "":
    print("Sisestage allpool koogi nime, millise hinda soovite arvutada.")
    nimi = input("šokolaadikook, ploomikook, Napoleooni kook: ")
    while True:
        moot = input("Millise mõõduga kooki soovite: ")
        if float(moot) < 0:
            print("\nSisestage korralik hind.\n")
            continue
        else:
            break
    
    
hind = koogi_hind(nimi, moot)

if hind != False:
    print("Koogi hind on ", hind)
