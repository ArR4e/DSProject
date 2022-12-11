def seosta_lapsed_ja_vanemad(x, y):
    seosed = {}
    f = open("lapsed.txt", encoding = "utf-8")
    g = open("nimed.txt", encoding = "utf-8")
    nimed = []
    for rida in g:
        kood, nimi = rida.strip().split(' ',1)
        nimed.append((kood, nimi))
    g.close()       
    for rida in f:
        vanem, laps = rida.strip().split(' ')
        for element in nimed:
            if vanem in element:
                vanema_nimi = element[1]
            if laps in element:
                lapse_nimi = element[1]
        if lapse_nimi not in seosed:
            seosed[lapse_nimi] = set([vanema_nimi])
        else:
            x = list(seosed[lapse_nimi])
            x.append(vanema_nimi)
            x = set(x)
            seosed[lapse_nimi] = x
    return seosed

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))