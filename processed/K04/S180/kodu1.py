from math import pi

while True:
    def koogi_hind(x, y):
        if x == 'šokolaadikook':
            return (pi * y ** 2) * 0.06
        elif x == 'ploomikook':
            return (pi * y ** 2) * 0.04
        elif x == 'Napoleoni kook':
            return y ** 2 * 0.1
        else:
            raise ValueError("Sellist kooki andmebaasist ei leitud")
    
    x = input('Sisesta koogi nimi: ')
    if x =="":
        break
    y = float(input('Sisesta koogi mõõt: ')) 
    z = koogi_hind(x, y)
    print('Koogi hind on', round(koogi_hind(x, y), 2), '€.')