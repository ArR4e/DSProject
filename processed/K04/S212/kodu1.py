from math import pi

def koogi_hind(name,size):
    if not name in cakes:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    elif name == cakes[0]:
        return round(size**2*pi*0.06,2)
    elif name == cakes[1]:
        return round(size**2*pi*0.04,2)
    elif name == cakes[2]:
        return round(size**2*0.1,2)


cakes = ["šokolaadikook", "ploomikook", "Napoleoni kook"]

while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == '':
        break
    suurus = float(input("Sisestage koogi mõõt: "))
    print("Koogi hind on ",str(koogi_hind(nimi,suurus)) + "€")