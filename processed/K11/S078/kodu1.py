def seosta_lapsed_ja_vanemad(fail_1, fail_2):
    sõnastik = {}
    tulemus = {}
    laste_fail = open(fail_1, 'r', encoding='UTF-8')
    nimede_fail = open(fail_2, 'r', encoding='UTF-8')
    for rida in nimede_fail:
        vahe_rida = rida.split()
        sõnastik[vahe_rida[0]] = rida[len(vahe_rida[0])+1:].strip('\n')

    for rida in laste_fail:
        id_rida = rida.split()
        if id_rida[1] in sõnastik:
            lapse_nimi = sõnastik[id_rida[1]]
            vanema_nimi = sõnastik[id_rida[0]]
            if lapse_nimi not in tulemus:
                tulemus[lapse_nimi] = set()
            tulemus[lapse_nimi].add(vanema_nimi)
            
    return tulemus

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))