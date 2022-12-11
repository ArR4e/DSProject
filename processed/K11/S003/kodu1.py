def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f = open(nimed)
    dnimed = {}
    for rida in f:
        nimijaisikukood = rida.strip("\n").split(" ",1)
        dnimed[nimijaisikukood[0]] = nimijaisikukood[1]
        
    f.close()
    f = open(lapsed)
    dvanemad = {}
    for rida in f:
        isikukoodid = rida.strip("\n").split(" ")
        if dnimed[isikukoodid[1]] not in dvanemad.keys():
            dvanemad[dnimed[isikukoodid[1]]] = set()
        dvanemad[dnimed[isikukoodid[1]]].add(dnimed[isikukoodid[0]])
        
    return dvanemad