from math import *

nimi = str(input('Millist kooki soovite?'))
suurus = float(input('Kui suurt?'))


def koogi_hind(nimi, suurus) :
    while True:
        if nimi != 'šokolaadikook' and nimi != 'ploomikook' and nimi != 'Napoleoni_kook' :
            raise Exception('Sellist kooki meil andmebaasist ei leidu.')
        elif nimi == '':
            break
        elif nimi == 'šokolaadikook' :
            return round((0.06 * ( pi * suurus ** 2)), 2)
            print('Maksta tuleb ', koogi_hind(nimi, suurus), ' eurot.')
        elif nimi == 'ploomikook' :
            return round((0.04 * (pi * suurus ** 2)), 2)
            print('Maksta tuleb ', koogi_hind(nimi, suurus), ' eurot.')
        elif nimi == 'Napoleoni_kook' :
            return round((0.1 * suurus ** 2), 2)
            print('Maksta tuleb ', koogi_hind(nimi, suurus), ' eurot.')