def seosta_lapsed_ja_vanemad(lasteFail, nimedeFail):
    
    nimed = open(nimedeFail, 'r')
    lapsed = open(lasteFail, 'r')

    isikukoodid = {}
    sonastik = {}

    for rida in nimed:

        rida = rida.strip()
        isikukoodid[rida[0:11]] = rida[12:len(rida)]

    for rida in lapsed:

        rida = rida.strip()
        a = rida.split()
        
        vanemadSet = {isikukoodid[a[0]]}
        
        if isikukoodid[a[1]] in sonastik.keys():
            sonastik[isikukoodid[a[1]]].add(isikukoodid[a[0]])
        else:
            sonastik[isikukoodid[a[1]]] = vanemadSet
        
    return sonastik