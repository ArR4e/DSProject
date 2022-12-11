def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for nimi in järjend:
        if nimi.endswith('P'):
            poisid += 1
        elif nimi.endswith('T'):
            tüdrukud += 1
    return (poisid, tüdrukud)
