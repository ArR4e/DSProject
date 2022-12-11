def seosta_lapsed_ja_vanemad(lapsedfail,nimedfail):
    tulemus = {}
    lastevanemad = {}
    nimed = {}
    with open(lapsedfail) as f:
        for i in f.readlines():
            i = i.strip().split()
            if i[1] in lastevanemad:
                lastevanemad[i[1]].append(i[0])
            else:
                lastevanemad[i[1]] = [i[0]]
    with open(nimedfail) as f:
        for i in f.readlines():
            i = i.strip().split()
            nimed[i[0]] = " ".join(i[1:len(i)])
    for laps in lastevanemad:
        for vanem in lastevanemad[laps]:
            if nimed[laps] in tulemus:
                tulemus[nimed[laps]].add(nimed[vanem])
            else:
                tulemus[nimed[laps]] = set([nimed[vanem]])
    return tulemus
tulemus = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
for laps in tulemus:
    print(f"{laps}: {', '.join(list(tulemus[laps]))}")