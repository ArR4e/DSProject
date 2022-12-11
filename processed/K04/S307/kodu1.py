from math import pi

koogid = ["šokolaadikook" , "ploomikook" , "Napoleoni kook"]
a = 1

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return(round((mõõt ** 2) * pi * 0.06, 2))
    elif nimi == "ploomikook":
        return(round((mõõt ** 2) * pi * 0.04, 2))
    elif nimi == "Napoleoni kook":
        return(round((mõõt ** 2) * 0.10, 2))
    elif nimi not in koogid:
        raise Exception("Sellist kooki andmebaasis ei leitud")


while a < 2:
    nimi = input("Sisestage koogi nimi")
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisestage mõõt"))
        print(koogi_hind(nimi, mõõt), "eurot")
