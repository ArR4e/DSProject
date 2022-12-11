def seosta_lapsed_ja_vanemad(fail1, fail2):
    l = open(fail1, encoding = 'UTF-8')
    n = open(fail2, encoding = 'UTF-8')
    nimed = {}
    isikukoodid = []
    seosed = {}
    for kombinatsioon in l:
        isikukood = kombinatsioon.strip().split(" ")
        isikukoodid += isikukood
    for komplekt in n:
        nimi = komplekt.strip().split(" ", 1)
        nimed[nimi[0]] = nimi[1]
    for i in range(1, len(isikukoodid), 2):
        if nimed[isikukoodid[i]] not in seosed:
            seosed[nimed[isikukoodid[i]]] = set()
    for i in range(1, len(isikukoodid), 2):
        if nimed[isikukoodid[i]] in seosed.keys():
            seosed[nimed[isikukoodid[i]]].add(nimed[isikukoodid[i-1]])

    return seosed
    l.close()
    n.close()

seotud = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for laps in seotud:
    if len(seotud[laps]) == 2:
        print(laps + ": " + seotud[laps].pop() + ", " + seotud[laps].pop())
    else:
        print(laps + ": " + seotud[laps].pop())

