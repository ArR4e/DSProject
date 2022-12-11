def poisse_ja_tüdrukuid(järjend):
    tüdruk = 0
    poiss = 0
    isikud = 0
    for nimi_sugu in järjend:
        nimi_ja_sugu = nimi_sugu.split()
        for sugu in nimi_ja_sugu:
            if sugu == 'T':
                tüdruk += 1
            elif sugu == 'P':
                poiss += 1
            else:
                continue
    return (poiss, tüdruk)
