def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik = {}
    with open(lapsed, encoding = 'utf-8') as f:
        laps = []
        vanem = []
        while True:
            g = f.readline()
            if g == '':
                break
            sisu = g.split()
            laps.append(sisu[1])
            vanem.append(sisu[0])
        f.close()
    nimi = {}
    with open(nimed, encoding = 'utf-8') as a:
        while True:
            b = a.readline().strip()
            if b == '':
                break
            sisu_1 = b.split(' ', 1)
            nimi[sisu_1[0]] = sisu_1[1]
    a.close()
    vanemad = []
    for lapsuke in laps:
        indeksid = [x for x, i in enumerate(laps) if i == lapsuke]
        for y in indeksid:
            vanemad.append(nimi[vanem[y]])
        sõnastik[nimi[lapsuke]] = set(vanemad)
        vanemad.clear()
    
    return sõnastik

sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for võti in sõnastik:
    print(võti + ': ' + str(', '.join(sõnastik[võti])))
    
    
    
    
    