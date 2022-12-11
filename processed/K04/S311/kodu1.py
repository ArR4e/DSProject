from math import pi
def koogi_hind(n, m):
    if n == "šokolaadikook":
        return(round(pi*(m**2)*0.06,2))
    elif n == "Napoleoni kook":
        return(round((m**2)*0.1,2))
    elif n == "ploomikook":
        return(round(pi*(m**2)*0.04,2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    nim = input("Sisesta koogi nimi: ")
    if nim != "":
        mõõt = float(input("Sisesta koogi mõõt: "))
        print("Koogi hind on", koogi_hind(nim, mõõt), "eurot.")
    else:
        break
        
