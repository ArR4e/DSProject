from math import pi


def f(tüüp, suurus):
    if tüüp == "šokolaadikook":
        hind = suurus * suurus * pi * 0.06
        return hind
    elif tüüp == "ploomikook":
        hind = suurus * suurus * pi * 0.04
        return hind
    elif tüüp == "Napoleoni kook":
        hind = suurus * suurus * 0.1
        return hind
    else:
        return 0


tüüp = str(input("Mis kooki tahad?: "))
suurus = float(input("Mis suurust tahad (cm): "))
x = f(tüüp, suurus)
if x != None and x!= 0:
    print("sinu kook maksab " + str(round(x, 2)) + " eurot")
else:
    print("Sellist kooki andmebaasist ei leitud")

    