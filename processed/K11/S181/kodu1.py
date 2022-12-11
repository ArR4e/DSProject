def seosta_lapsed_ja_vanemad(lapsed,nimed):
    sõnastik = {}
    nimed_s = {}
    lapsed_list = []
    lapsed_vanemad = {}
    f1 = open(lapsed)
    f2 = open(nimed)
    for i in f2.read().splitlines():
        j = i.split(" ",1)
        nimed_s[j[0]] = j[1]
    for x in f1.read().split():
        if x in nimed_s:
            lapsed_list.append(nimed_s[x])
    for x in range(int(len(lapsed_list)*0.5)):
        if lapsed_list[2*x+1] in lapsed_vanemad:
            lapsed_vanemad[lapsed_list[2*x+1]].add(lapsed_list[2*x])
        else:
            lapsed_vanemad[lapsed_list[2*x+1]] = set()
            lapsed_vanemad[lapsed_list[2*x+1]].add(lapsed_list[2*x])
    f1.close()
    f2.close()
    return lapsed_vanemad