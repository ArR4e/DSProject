from math import pi
while True:
    koogi_nimi = str(input("Kirjuta soovitud koogi nimetus: "))
    if koogi_nimi == "":
        break
    raadius = float(input("Sisesta soovitud koogi mõõt(raadius sentimeetrites): ")) 
    def koogi_hind(koogi_nimi, raadius):
        if koogi_nimi == "Napoleoni kook":
            koogi_maksumus = raadius ** 2 * 0.06
        elif koogi_nimi == "ploomikook":
            koogi_maksumus = raadius ** 2 * 0.04 * pi 
        elif koogi_nimi == "šokolaadikook":
            koogi_maksumus = raadius ** 2 * 0.10 * pi
        return round(float(koogi_maksumus), 2)
    try:
        print("Koogi hind on", koogi_hind(koogi_nimi, raadius), "eurot")
    except:
        print("Sellist kooki andmebaasist ei leitud")
