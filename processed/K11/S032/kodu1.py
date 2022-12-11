def seosta_lapsed_ja_vanemad(lapsed, nimed):
    l = open(lapsed)
    n = open(nimed)
    isikukood = {}
    for rida in n:
        rida = [rida[:11], rida[11:].strip()]
        isikukood[rida[0]] = rida[1]
    seosed = {}
    for rida in l:
        rida = rida.strip().split()
        if isikukood[rida[1]] in seosed:
            seosed[isikukood[rida[1]]].add(isikukood[rida[0]])
        else:
            seosed[isikukood[rida[1]]] = {isikukood[rida[0]]}
    l.close()
    n.close()
    return seosed

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))

