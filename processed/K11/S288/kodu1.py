def seosta_lapsed_ja_vanemad(fail1, fail2):
    lapsed = {}
    nimed = {}
    sõnastik = {}
    with open(fail1, encoding = 'UTF-8') as f1:
        for rida in f1:
            rida = rida.strip().split(' ')
            lapsed[rida[1]] = set()
    with open(fail1, encoding = 'UTF-8') as f1:
        for rida in f1:
            rida = rida.strip().split(' ')
            lapsed[rida[1]].add(rida[0])
    with open(fail2, encoding = 'UTF-8') as f2:
        for rida in f2:
            rida = rida.strip().split(' ')
            nimed[rida[0]] = rida[1] + ' ' + rida[2]
    for i in lapsed:
        laps = nimed.get(i)
        sõnastik[laps] = set()
    for j in lapsed:
        for x in lapsed.get(j):
            laps = nimed.get(j)
            vanem = nimed.get(x)
            sõnastik[laps].add(vanem)
    for y in sõnastik:
        print(y + ': ' + str(sõnastik.get(y)).replace('{', '').replace('}', '').replace("'", ''))
    return sõnastik