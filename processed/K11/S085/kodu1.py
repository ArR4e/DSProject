def seosta_lapsed_ja_vanemad(fail1, fail2):
    järjend = []
    sõnastik = {}
    a = {}
    f = open("lapsed.txt")
    f1 = open("nimed.txt")
    for rida in f:
        isikukood = rida.strip().split(' ')
        järjend.append(isikukood)
    for rida in f1:
        nimed = rida.strip().split(" ", 1)
        sõnastik[nimed[0]] = nimed[1]
    for el in järjend:
        if sõnastik[el[1]] in a:
            a[sõnastik[el[1]]].add(sõnastik[el[0]])
        else:
            a[sõnastik[el[1]]] = set()
            a[sõnastik[el[1]]].add(sõnastik[el[0]])
    return a
    f.close()
    f1.close()

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in sõnastik:
    nimi = list(sõnastik[võti])
    if len(sõnastik[võti]) == 2:
        print(võti+":",nimi[0]+", "+nimi[1])
    else:
        print(võti+":", nimi[0])