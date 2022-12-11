def seosta_lapsed_ja_vanemad(fail1, fail2):
    f = open(fail1, 'r', encoding='UTF-8')
    g = open(fail2, 'r', encoding='UTF-8')
    Mydict1 = {}
    Mydict = {}
    for rida in g:
        rida = rida.strip('\n').split()
        Mydict1[rida[0]] = rida[1] + ' ' + rida[2]
    g.close()
    for rida in f:
        rida = rida.strip('\n').split()
        try:
            Mydict[Mydict1[rida[1]]].add(Mydict1[rida[0]])
        except:
            Mydict[Mydict1[rida[1]]] = {Mydict1[rida[0]]}
    f.close()
    return(Mydict)
for laps, vanemad in seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt').items():
    print(laps + ':', ', '.join(vanemad))