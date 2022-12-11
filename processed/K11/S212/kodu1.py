def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    lapsed = []
    nimed = {}
    f = open(lastefail, encoding='utf8')
    i=0
    for rida in f:
        lapsed.append([])
        vanem, laps = rida.strip().split()
        lapsed[i].append(vanem)
        lapsed[i].append(laps)
        i+=1
    f.close()
    f = open(nimedefail, encoding='utf8')
    for rida in f:
        laps, nimi = rida.strip().split(' ',1)
        nimed[laps] = nimi
    sonastik = {}
    for key1 in lapsed:
        for key2 in nimed:
            if key1[1]==key2:
                if nimed[key2] in sonastik:
                    sonastik[nimed[key2]].add(nimed[key1[0]])
                else:
                    sonastik[nimed[key2]] = {nimed[key1[0]]}
    return sonastik
sonastik = (seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
for key in sonastik:
    parents = ''
    for parent in sonastik[key]:
        parents = parents + " " + parent
    parents = parents.strip()
    print(key + ': ' + parents)