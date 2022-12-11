from math import pi

def koogi_hind(name, size):
    if name == 'šokolaadikook':
        return round(pi*(size**2)*0.06, 2)
    elif name == 'ploomikook':
        return round(pi*(size**2)*0.04, 2)
    elif name == 'Napoleoni kook':
        return round((size**2)*0.10, 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')

while True:
    pie_name = input('Sisesta koogi nimi: ')
    if not pie_name:
        break
    pie_size = float(input('Sisesta koogi mõõt: '))
    pie_price = koogi_hind(pie_name, pie_size)
    print('Koogi hind on', pie_price, 'eurot')