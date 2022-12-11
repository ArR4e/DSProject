from math import pi

kooginimi = input('Sisesta koogi nimi: ')
mõõtmed = int(input('Sisetsa mõõtmed: '))

def koogi_hind(kooginimi, mõõtmed):

    if kooginimi == 'sokolaadikook':
       sokolaadikook = float((pi * mõõtmed ** 2) * 0.06)
       return sokolaadikook

    if kooginimi == 'ploomikook':
       ploomikook = float((pi * mõõtmed ** 2) * 0.04)
       return ploomikook

    if kooginimi == 'napoleonikook':
       napoleonikook = float((mõõtmed ** 2) * 0.10)
       return napoleonikook
    
    else:
        print('Sellist kooki andmebaasist ei leitud')
        
koogi_hind(kooginimi, mõõtmed)
print('Koogihind on',koogi_hind(kooginimi, mõõtmed), 'eurot')



