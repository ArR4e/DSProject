def seosta_lapsed_ja_vanemad(x, y):
    f1 = open(x)
    sõn = {}
    for rida in f1:
        abisõn = {}
        rida = rida.strip().split(' ',)
        for indeks in range(len(rida)):
            if abisõn == {}:
                laps = rida[indeks-1] #leian lapse isikukoodi
                f2 = open(y)
                for read in f2:#teisendan isikukoodi nimeks
                    read = read.strip().split(' ', 1)
                    if laps in read:
                        laps = read[1]
                    else:
                        continue
                f2.close() 
                abisõn[laps] = set()
                if laps not in sõn:
                    sõn[laps] = set() #sean lapse nime võtmeks
            else:
                f2 = open(y)
                for read in f2:
                    read = read.strip().split(' ', 1)
                    if rida[indeks-1] in read:
                        vanem = read[1]
                        sõn[laps].add(vanem) #lisan vanema nime(d) tühja hulga sisse
                    else:
                        continue
                f2.close()
    return sõn

lapsed_vanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for laps in lapsed_vanemad:
    print(laps + ': ' + ', '.join(lapsed_vanemad[laps]))
