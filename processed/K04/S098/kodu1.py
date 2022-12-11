#šokolaadikook, maasikakook, Napoleoni kook
from math import pi
kook = input("Mis kooki tahad? ")
suurus = float(input("Kui suur kook? "))

koogitüüp = [0.06, 0.04, 0.10]


def koogi_hind(*t):
    if kook == "šokolaadikook":
        g = koogitüüp[0]
        pindala = pi*r**2
    elif kook == "ploomikook":
        g = koogitüüp[1]
        pindala = pi*r**2
    elif kook == "Napoleoni kook":
        g = koogitüüp[2]
        pindala = r**2
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    return round(g*pindala, 2)
    
print(koogi_hind(g, suurus))