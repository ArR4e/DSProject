from math import pi
def koogi_hind(kooginimi, mõõt):
    if kooginimi==("šokolaadikook"):
        return round(pi*(mõõt**2)*0.06, 2)
    elif kooginimi==("ploomikook"):
        return round(pi*(mõõt**2)*0.04, 2)
    elif kooginimi==("Napoleoni kook"):
        return round(mõõt**2*0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
while True:
    kooginimi=input("Sisesta koogi nimi: ")
    if kooginimi== (""):
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(kooginimi,mõõt))
    