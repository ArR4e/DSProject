def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f = open(lapsed, 'r')
    g = open(nimed, 'r')
    lapsed_list = []
    nimed_dict = {}
    tulemus = {}

    for rida in f.readlines():
        rida = rida.split(' ')
        lapsed_list.append((rida[0].strip(), rida[1].strip()))

    for rida in g.readlines():
        rida = rida.split(' ')
        nimed_dict[rida[0].strip()] = ' '.join(list(map(str.strip, rida[1:])))

    for laps in lapsed_list:
        for kood in nimed_dict.keys():
            if kood == laps[1]:
                tulemus[list(nimed_dict.values())[list(nimed_dict.keys()).index(kood)]] = set()

    for laps in tulemus.keys():
        for paar in lapsed_list:
            if paar[1] == list(nimed_dict.keys())[list(nimed_dict.values()).index(laps)]:
                tulemus[laps].add(nimed_dict[paar[0]])

    f.close()
    g.close()
    return(tulemus)


tulemus = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for laps in tulemus.keys():
    rida = laps + ': ' + ', '.join(tulemus[laps])
    print(rida)