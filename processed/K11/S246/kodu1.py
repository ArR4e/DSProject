def seosta_lapsed_ja_vanemad(f1, f2):
    d = {}
    d1 = {}
    nimed = open(f2)
    for rida in nimed:
        jarjend = rida.strip().split(' ')
        jarjend[1 : 3] = [' '.join(jarjend[1 : 3])]
        d1[jarjend[0]] = jarjend[1]
    nimed.close()
    lapsed = open(f1)
    for rida in lapsed:
        jarjend = rida.strip().split(' ')
        laps = d1[jarjend[1]]
        vanem = d1[jarjend[0]]
        if laps not in d:
            d[laps] = set()
            d[laps].add(vanem)
        elif laps in d:
            d[laps].add(vanem)
    lapsed.close()
    return d

sonastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for el in sonastik:
    print(el + ': ', end='')
    if len(sonastik[el]) == 2:
        nimed = list(sonastik[el])
        print(nimed[0] + ', ' + nimed[1])
    else:
        nimi = list(sonastik[el])
        print(nimi[0])