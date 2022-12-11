def koogi_hind(nimi, suurus):
    nimi = input('Sisesta koogi nimi: ')
    if nimi == 'šokolaadikook' or 'ploomikook' or 'Napoleoni kook':
        return ('jätkake')
    else:
        raise Exception('Sellist koooki andmebaasis ei leidu.')
    suurus = int(input('Sisesta koogi raadius cm-tes: '))
    if suurus < 0:
        return ('Suurus ei saa olla negatiivne.')
    else:
        if nimi == 'Napoleoni kook':
            hind1 = suurus ** 2
            return ('koogi hind on: ', round(hind1, 2))
        else:
            hind2 = suurus ** 2 * 3.14
            return ('Koogi hind on ', round(hind2, 2))