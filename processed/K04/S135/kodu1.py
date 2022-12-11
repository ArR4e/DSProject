from math import pi

# funktsioon, mis arvutab ja väljastab hinna eurodes šokolaadikoogile, ploomikoogile
# ning Napoleoni koogile. Arvestan, et mõõt on sentimeetrites
def koogi_hind(koogiNimi, moot):
    if koogiNimi == "šokolaadikook":
            return round((moot**2 * pi) * 0.06, 2)
    elif koogiNimi == "ploomikook":
        return round((moot**2 * pi) * 0.04, 2)
    elif koogiNimi == "Napoleoni kook":
        return round(moot**2 * 0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

# arvutab koogi hinna kuni kasutaja ei sisesta midagi koogi nimena, siis katkestab
# tsükli
while True:
    koogiNimi = input("Sisesta koogi nimi ")
    if koogiNimi == "":
        break
    koogiMoot = float(input("Sisesta koogi mõõt "))

    print("Koogi hind on", koogi_hind(koogiNimi, koogiMoot), "€")
