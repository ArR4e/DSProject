def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
    # Laste ja vanemate isikukoodide eraldamine
    lapsed_f = open(lapsed_fail, 'r', encoding = 'UTF-8')
    lapsed = []
    vanemad = []
    for rida in lapsed_f:
        rida = rida.strip().split(' ', 1)
        if rida[1] not in lapsed:
            lapsed.append(rida[1])
        if rida[0] not in vanemad:
            vanemad.append(rida[0])

    # Isikukood nimega seostamine
    nimed_f = open(nimed_fail, 'r', encoding = 'UTF-8')
    lapsed_isikukoodidega = {}
    vanemad_isikukoodidega = {}
    for rida in nimed_f:
        rida = rida.strip().split(' ', 1)
        if rida[0] in lapsed:
            lapsed_isikukoodidega[rida[0]] = rida[1]
        if rida[0] in vanemad:
            vanemad_isikukoodidega[rida[0]] = rida[1]
    
    # Lapsed vanematega seostamine
    lapsed_f = open('lapsed.txt', 'r', encoding = 'UTF-8')
    lapsed_ja_vanemad = {}    
    for rida in lapsed_f:
        rida = rida.strip().split(' ', 1)
        if rida[1] in lapsed_isikukoodidega:
            lapse_nimi = lapsed_isikukoodidega[rida[1]]
            if lapse_nimi not in lapsed_ja_vanemad:
                lapsed_ja_vanemad[lapse_nimi] = set()
        if rida[0] in vanemad_isikukoodidega:
            vanema_nimi = vanemad_isikukoodidega[rida[0]]
        lapsed_ja_vanemad[lapse_nimi].add(vanema_nimi)
    
    lapsed_f.close()
    nimed_f.close()
    
    return lapsed_ja_vanemad

lapsed_ja_vanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for lapsed in lapsed_ja_vanemad:
    vanemad_sõnastik = lapsed_ja_vanemad[lapsed]
    vanemad = ''
    if len(lapsed_ja_vanemad[lapsed]) == 2:
        vanemad_järjend = []
        for vanem in vanemad_sõnastik:
            vanemad_järjend.append(vanem)
        print(lapsed + ': ' + vanemad_järjend[0] + ', ' + vanemad_järjend[1])
    else:
        for vanem in vanemad_sõnastik:
            vanemad += vanem
        print(lapsed + ': ' + vanemad)


# Seda peab saama kuidagi lihtsamalt teha...