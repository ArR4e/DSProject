from math import pi

def koogi_hind(name, size):
    if name.lower() == 'šokolaadikook':
        return round(size**2 * pi * 0.06, 2)
    elif name.lower() == 'ploomikook':
        return round(size**2 * pi * 0.04, 2)
    elif name.lower() == 'napoleoni kook':
        return round(size**2 * 0.1, 2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud.')


while True:
    cake_name = input('Sisestage koogi nimi: ')

    if cake_name == '':
        break

    cake_size = float(input('Sisestage koogi suurus: '))

    print(f'{cake_name} maksab {koogi_hind(cake_name, cake_size)} eurot')
    