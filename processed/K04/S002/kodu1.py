from math import pi
def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        return round((pi*mõõt**2)*0.06,2)
    elif nimi == "ploomikook":
        return round((pi*mõõt**2)*0.04,2)
    elif nimi == "Napoleoni kook":
        return round((mõõt**2)*0.1,2)
    else: raise Exception("Sellist kooki andmebaasist ei leitud")

n = input("Kook")
m = float(input("Mõõt"))

while True:
    print(koogi_hind(n,m))
    n = input("Kook")
    if n == "":
        break
    m = float(input("Mõõt"))