from math import pi


def koogi_hind(nimi, size):
    if nimi=="ploomikook":
        return(round(pi*(size**2)*0.04, 2))
    elif nimi=="šokolaadikook":
        return(round(pi*(size**2)*0.06, 2))
    elif nimi=="Napoleoni kook":
        return(round((size**2)*0.10, 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

while True:
    ae = input(str("Sisesta koogi nimi: "))
    if not ae:
        break
    ea = input("Sisesta koogi suurus: ")
    ea = float(ea)
    print(koogi_hind(ae,ea))