def seosta_lapsed_ja_vanemad(lapsed, nimed):
    pered = {}
    lapsed = open(lapsed)
    nimed = open(nimed)
    dictNimed = {}
    for nimi in nimed.readlines():
        nimi = nimi.split()
        dictNimed[nimi[0]] = ' '.join(nimi[1:])
    for line in lapsed.readlines():
        n = line.split()
        if dictNimed[n[1]] in pered:
            pered[dictNimed[n[1]]].add(dictNimed[n[0]])
        else:
            pered[dictNimed[n[1]]] = {dictNimed[n[0]]}
    return pered

pered = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for laps in pered:
    vanemad = ''
    for vanem in pered[laps]:
        if vanemad == '':
            vanemad = vanem
        else:
            vanemad += ', ' + vanem
    print(laps + ': ' + vanemad)