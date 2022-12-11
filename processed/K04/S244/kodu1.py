import math 

def koogi_hind(nimi, mõõt):

    if nimi == "ploomikook":
        return(round((mõõt **2) * math.pi * 0.04, 2))
    elif nimi == "šokolaadikook":
        return(round((mõõt **2) * math.pi * 0.06, 2))
    elif nimi == "Napoleoni kook":
        return(round((mõõt ** 2) * 0.10, 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

        

while True:
    try:
        nimi = input("Sisestage koogi nimi: ")
        if nimi == "":
            break
        mõõt = float(input("Sisesta koogi mõõt: "))
        print("Koogi hind on " + str(koogi_hind(nimi, mõõt)) + " eurot.")
    except:
        print("Sellist kooki andmebaasist ei leitud")

    
    
    
    