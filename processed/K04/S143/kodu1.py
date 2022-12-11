from math import pi
def koogi_hind(n,m):
    if n=="šokolaadikook":
        return round(m**2*pi*0.06,2)
    elif n=="ploomikook":
        return round(m**2*pi*0.04,2)
    elif n=="Napoleoni kook":
        return round(m**2*0.10,2)
    elif n=="":
        return n
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
        return n

while(True):
    a=input("Sisesta koogi nimi: ")
    if a=="":
        break
    print(koogi_hind(a,float(input("Sisesta koogi mõõt: "))))