from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return(round(pi*(mõõt**2)*0.06,2))
    elif nimi == "ploomikook":
        return(round(pi*(mõõt**2)*0.04,2))
    elif nimi == "Napoleoni kook":
        return(round((mõõt**2)*0.10,2))
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")

while True:
    nimii = input("Sisesta koogi nimi: ")
    if nimii != "":
        mõõtt = float(input("Sisesta koogi mõõt: "))
        print("Koogi hind on",koogi_hind(nimii, mõõtt),"eurot.")
    else:
        break