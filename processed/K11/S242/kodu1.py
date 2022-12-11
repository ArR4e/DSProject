
def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    koodid = {}
    inimene_kood = {}
    tulemus = {}
    lastefail = open('lapsed.txt', encoding='UTF-8')
    nimedefail = open('nimed.txt', encoding='UTF-8')
    for rida in lastefail:
        vanem_laps = rida.strip().split(' ')
        vanem = vanem_laps[0]
        laps = vanem_laps[1]
        if vanem not in koodid.keys():
            koodid[vanem] = set()
        koodid[vanem].add(laps)
    for rida in nimedefail:
        inimene = rida.strip().split(' ', 1)
        nimi = inimene[1]
        isikukood = inimene[0]
        inimene_kood[isikukood] = nimi
    for vanem, lapsed in koodid.items():
        vanema_nimi = inimene_kood[vanem]
        for laps in lapsed:
            lapse_nimi = inimene_kood[laps]
            if lapse_nimi not in tulemus.keys():
                tulemus[lapse_nimi] = set()
            tulemus[lapse_nimi].add(vanema_nimi)
    return tulemus
        
for laps, vanemad in seosta_lapsed_ja_vanemad('lapsed.txt', 'vanemad').items():
    vanemaid = 0
    vanemate_loend = []
    for vanem in vanemad:
        vanemaid += 1
        vanemate_loend.append(vanem)
    if vanemaid == 1:
        print(laps + ': ' + vanemate_loend[0])
    elif vanemaid == 2:
        print(laps + ': ' + vanemate_loend[0] + ', ' + vanemate_loend[1])

        