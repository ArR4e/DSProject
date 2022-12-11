def koogi_hind(nimi, moot):
    moot = float(moot)
    if nimi == 'šokolaadikook':
        mooduhind = 0.06
    elif nimi == 'ploomikook':
        mooduhind = 0.04
    elif nimi == 'Napoleoni kook':
        mooduhind = 0.1
    else:
        raise Exceprion('Sellist kooki andmebaasist ei leitud')
        
    hind = round(mooduhind*moot, 2)
    return hind


while True:
    name = input('Sisestage koogi nimi: ')
    if name == '':
        break
    suurus = input('Sisestage koogi mõõdu: ')

    hind = koogi_hind(name, suurus)
    print('Koogi hind on', hind, '€')
