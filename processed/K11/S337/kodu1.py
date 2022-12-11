def seosta_lapsed_ja_vanemad(f1, f2):
    nimed = {}
    vastus = {}
    f = open(f2)
    for rida in f:
        rida = rida.strip('\n').split(' ', 1)
        nimed[rida[0]]=rida[1]
    f.close()
    f = open(f1)
    for rida in f:
        rida = rida.split()
        if nimed[rida[1]] not in vastus:
            vastus[nimed[rida[1]]] = set()
            vastus[nimed[rida[1]]].add(nimed[rida[0]])
        else:
            vastus[nimed[rida[1]]].add(nimed[rida[0]])
    return vastus