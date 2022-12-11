def koogi_hind(nimi, size):
    if not (nimi == "šokolaadikook" or nimi == "ploomikook" or nimi == "Napoleoni kook"):
        raise Exception("Sellist kooki andmebaasist ei leitud")
    elif size < 0:
        raise Exception("Sisesta õige mõõt!")
    else:
        # error checkid möödas, õige kood
        if nimi == "šokolaadikook":
            # leian pindala et hind arvutada.
            arvutus = 3.14 * (size * size)
            # hind 2 komakohani, korrutame pindala hinnaga.
            hind = round(arvutus * 0.06, 2)
        elif nimi == "ploomikook":
            arvutus = 3.14 * (size * size)
            hind = round(arvutus * 0.04, 2)
        elif nimi == "Napoleoni kook":
            arvutus = size * size
            hind = round(arvutus * 0.10, 2)
        print(hind)

nimi = input("Sisesta koogi nimi: ")
while(nimi == ""):
    nimi = input("Sisesta koogi nimi: ")
size = float(input("Sisesta koogi mõõt: "))

koogi_hind(nimi, size)