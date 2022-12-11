while True:
    try:
        koogi_nimi = input("Sisesta koogi nimi: ")
    except:
        continue
    else:
        if koogi_nimi != '':
            break

suurus = float(input("Sisesta koogi suurus ruutsentimeetrites: "))

def koogi_hind(koogi_nimi, suurus):    
    if koogi_nimi == "šokolaadikook":
        return suurus * 0.06
    elif koogi_nimi == "ploomikook":
        return suurus * 0.04
    elif koogi_nimi == "Napoleoni kook":
        return suurus * 0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud!")

hind = koogi_hind(koogi_nimi, suurus)
print("Koogi hinnaks tuleb " + str(round(hind, 2)) + " eurot")