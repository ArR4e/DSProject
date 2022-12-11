from math import pi

def koogi_hind(name, size):
    name = name.lower()
    if name == str('šokolaadikook'):
        return(round((pi * size ** 2 * 0.06), 2))
    elif name == str('ploomikook'):
        return(round((pi * size ** 2 * 0.04), 2))
    elif name == str('napoleoni kook'):
        return(round((size ** 2 * 0.1), 2))
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    name = str(input('Kirjuta koogi nimi siia : '))
    if name == str(''):
        break
    size = float(input('Kirjuta koogi külje pikkus/raadius: '))
    print(koogi_hind(name, size))