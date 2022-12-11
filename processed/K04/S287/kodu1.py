kook = input("Sisestage koogi nimi: ")
suurus = float(input("Sisestage koogi suurus: "))

euro = 0
suur = 0

if kook == "sokolaadikook" or kook == "šokolaadikook":
    euro = 0.06
elif kook == "ploomikook":
    euro = 0.04
elif kook == "Napoleoni kook" or kook == "napoleoni kook":
    euro = 0.1
else:
    print("Sellist kooki andmebaasist ei leitud.")
    quit()

def koogi_hind(kook,euro,suur):
    if kook == "soklaadikook" or kook == "šokolaadikook" or kook == "ploomikook":
        hind = π * suurus * suurus * euro
        return(hind)
    else:
        hind = suurus * suurus * euro
        return(hind)
print(f"Koogi hind on {round(koogi_hind(kook,euro,suur), 2)} eurot")
    
    

