def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f1 = open(lapsed, encoding = 'UTF-8')
    f2 = open(nimed, encoding = 'UTF-8')
    ID_nimi_sõnastik = {}
    sõnastik = {}
    for rida in f2:
        rida_ok = rida.strip().split()
        ID_nimi_sõnastik[rida_ok[0]] = rida_ok[1] + ' ' + rida_ok[2]
    for rida in f1:
        rida_ok = rida.strip().split()
        lapse_nimi = ID_nimi_sõnastik[rida_ok[1]]
        vanema_nimi = ID_nimi_sõnastik[rida_ok[0]]
        if lapse_nimi not in sõnastik:
            sõnastik[lapse_nimi] = set()
            sõnastik[lapse_nimi].add(vanema_nimi)
        else:
            sõnastik[lapse_nimi].add(vanema_nimi)
    f1.close()
    f2.close()
    return sõnastik

sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for võti in sõnastik:
    vanemad = list(sõnastik[võti])
    if len(sõnastik[võti]) == 2:
        print(võti + ': ' + vanemad[0] + ', ' + vanemad[1])
    else:
        print(võti + ': ' + vanemad[0])