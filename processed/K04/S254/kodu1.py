from math import pi

def koogi_hind(nimi,mõõt):
    mõõt = float(mõõt)
    if nimi == 'šokolaadikook':
        pindala = pi*mõõt*mõõt
        maksumus = pindala * 0.06
        return round(maksumus,2)
    elif nimi == 'ploomikook':
        pindala = pi*mõõt*mõõt
        maksumus = pindala * 0.04
        return round(maksumus,2)
    elif nimi == 'Napoleoni kook':
        pindala = mõõt*mõõt
        maksumus = pindala * 0.10
        return round(maksumus,2)
    else:
        raise Exception('Sellist kooki andmebaasist ei leitud')

def sisend():
    while True:
        nimi = str(input('Sisetage koogi nimi: '))
        if nimi == '':
            break
        mõõt = input('Sisetage koogi mõõt: ')
        print('Koogi hind on:',koogi_hind(nimi,mõõt),'Eurot.')

sisend()