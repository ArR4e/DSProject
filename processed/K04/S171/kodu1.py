from math import*
def koogi_hind(liik, moot):
    if(liik == "šokolaadikook"):
        s = pi*(moot**2)
        return round(s * 0.06, 2)
    elif(liik == "ploomikook"):
        s = pi*(moot**2)
        return round(s * 0.04, 2)
    elif(liik == "Napoleoni kook"):
        s = moot**2
        return round(s * 0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasis ei leitud")
while True:
    a = input("Sisesta koogi nimi:")
    if a == "":
        break
    else:
        b = float(input("Sisesta koogi mõõt:"))
        print(koogi_hind(a,b))
