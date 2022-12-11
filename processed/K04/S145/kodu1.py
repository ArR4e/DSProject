import math

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook" or nimi == "ploomikook":
        r = float(mõõt)
        S = math.pi * r ** 2
        if nimi == "šokolaadikook":
            print(round(S * 0.06, 2))
            return round(S * 0.06, 2)
        elif nimi == "ploomikook":
            print(round(S * 0.04, 2))
            return round(S * 0.04, 2)
    elif nimi == "Napoleoni kook":
        r = float(mõõt)
        S = r ** 2
        print(round(S * 0.1, 2))
        return round(S * 0.1, 2)
    elif nimi != "šokolaadikook" or nimi != "ploomikook" or nimi != "Napoleoni kook":
        raise ValueError("Sellist kooki andmebaasist ei leitud")
nlist = []
mlist = []
while True:
    n = input("Sisestage koogi nimi: ")
    if n != "":
        m = input("Sisestage koogi mõõt sentimeetrites: ")
        nlist.append(n)
        mlist.append(m)
    else:
        break
    
for i in range(len(nlist)):
    koogi_hind(nlist[i], mlist[i])