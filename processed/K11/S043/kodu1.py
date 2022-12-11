def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    l = open(lastefail)
    lapsjavanem = []
    for rida in l:
        rida = rida.strip().split()
        lapsjavanem.append(rida)
    nim = open(nimedefail)
    nimed = []
    for rida in nim:
        rida = rida.strip().split(' ', 1)
        nimed.append(rida)
    nimed_s = dict([tuple(x) for x in nimed])
    laps_ja_vanem_nimedega = []
    for x in lapsjavanem:
        laps_ja_vanem_nimedega.append([nimed_s[x[0]], nimed_s[x[1]]])
    lõpusõnastik = dict()
    for laps, vanem in laps_ja_vanem_nimedega:
        try:
            lõpusõnastik[vanem].add(laps)
        except KeyError:
            lõpusõnastik[vanem] = {laps}
    
    return lõpusõnastik

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))