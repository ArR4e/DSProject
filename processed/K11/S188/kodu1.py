def seosta_lapsed_ja_vanemad(isikukoodid, nimed):
    laste_vanemate_sonastik = {}
    isikukoodide_sonastik = {}
    with open(nimed) as f:
        for rida in f:
            info = rida.strip().split(' ', 1)
            isikukoodide_sonastik[info[0]] = info[1]
    with open(isikukoodid) as g:
        for rida in g:
            seosed = rida.strip().split()
            laps = isikukoodide_sonastik[seosed[1]]
            vanem = isikukoodide_sonastik[seosed[0]]
            if laps not in laste_vanemate_sonastik:
                laste_vanemate_sonastik[laps] = {vanem}
            elif laps in laste_vanemate_sonastik:
                laste_vanemate_sonastik[laps].add(vanem)
    return laste_vanemate_sonastik

lapsed_ja_vanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for element in lapsed_ja_vanemad.keys():
    print(element + ': ' + ', '.join(lapsed_ja_vanemad[element]))