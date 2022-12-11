def seosta_lapsed_ja_vanemad(a,b):
    f1 = open(a, encoding = "UTF-8")
    f2 = open(b, encoding = "UTF-8")
    lapsed = {}
    nimed = {}
    vahepealne = []
    vastus = {}
    for rida in f1:
        isikuk = rida.strip("\n").split(" ")
        lapsed[isikuk[0]] = isikuk[1]
    for rida in f2:
        isikuk = rida.strip("\n").split(" ", 1)
        nimed[isikuk[0]] = isikuk[1]
    for isikuk in lapsed:
        vahepealne.append([nimed[isikuk], nimed[lapsed[isikuk]]])
    for nimi in vahepealne:
        vastus[nimi[1]] = set()
    for nimi in vahepealne:
        vastus[nimi[1]].add(nimi[0])
    return(vastus)
    f1.close()
    f2.close()
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")