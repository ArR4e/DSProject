fail1 = open("lapsed.txt", "r", encoding = "UTF-8")
fail2 = open("nimed.txt", "r", encoding = "UTF-8")
def seosta_lapsed_ja_vanemad(x, y):
    kõik = {}
    lapsed = {}
    tühjad = {}
    vanemad = {}
    isikukoodid = []
    for rida in fail2:
        b = rida.strip().split(" ", 1)
        kõik[b[0]] = b[1]
    for rida in fail1:
        a = rida.strip().split(" ")
        if a[1] not in lapsed:
            lapsed[a[1]] = kõik[a[1]]
        if a[1] in lapsed:
            lapsed[a[1]] = lapsed[a[1]]
        isikukoodid.append(a)
    for rida in lapsed:
        if lapsed[rida] not in tühjad:
            tühjad[lapsed[rida]] = set()
        if lapsed[rida] in tühjad:
            tühjad[lapsed[rida]] = tühjad[lapsed[rida]]
    for rida in isikukoodid:
        tühjad[tühjad[lapsed[rida[1]]].add(kõik[rida[0]])] = tühjad[lapsed[rida[1]]].add(kõik[rida[0]])
    tühjad.pop(None)
    return tühjad