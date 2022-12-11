def seosta_lapsed_ja_vanemad(fail1 = 'lapsed.txt', fail2 = 'nimed.txt'):
    lopp = {}
    f = open(fail1, 'r', encoding='UTF-8')#vanema isikukood ja lapse isikukood
    g = open(fail2, 'r', encoding='UTF-8')#isikukood, nimi
    nimed = []
    for rida in g:
        kood, nimi = rida.strip().split(' ', 1)
        nimed.append((nimi, kood))
    g.close()
    for rida in f:
        vanem, laps = rida.strip().split(' ', 1)
        for el in nimed:
            if vanem == el[1]:
                vanemaNimi = el[0]
            if laps == el[1]:
                lapseNimi = el[0]
        if lapseNimi not in lopp:
            lopp[lapseNimi] = set([vanemaNimi])
        else:
            x=list(lopp[lapseNimi])
            x.append(vanemaNimi)
            x = set(x)
            lopp[lapseNimi] = x
    return lopp
