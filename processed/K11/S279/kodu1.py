def seosta_lapsed_ja_vanemad(fail1, fail2):
    lapsed_fail = open(fail1, encoding="UTF-8")
    nimed_fail = open(fail2, encoding="UTF-8")
    
    lapsed_ja_vanemad = {}
    isikukood_ja_nimi = {}
    
    for rida in nimed_fail:
        isikukood_nimega_järjend = rida.strip().split(" ", 1)
        isikukood = isikukood_nimega_järjend[0]
        nimi = isikukood_nimega_järjend[1]
        isikukood_ja_nimi[isikukood] = nimi
    
    for rida in lapsed_fail:
        mõlema_isikukoodi_järjend = rida.strip().split(" ")
        vanema_isikukood = mõlema_isikukoodi_järjend[0]
        lapse_isikukood = mõlema_isikukoodi_järjend[1]
        vanema_nimi = isikukood_ja_nimi[vanema_isikukood]
        lapse_nimi = isikukood_ja_nimi[lapse_isikukood]
        if lapse_nimi not in lapsed_ja_vanemad:
            lapsed_ja_vanemad[lapse_nimi] = set()
            lapsed_ja_vanemad[lapse_nimi].add(vanema_nimi)
        else:
            lapsed_ja_vanemad[lapse_nimi].add(vanema_nimi)

    lapsed_fail.close()
    nimed_fail.close()
    return lapsed_ja_vanemad