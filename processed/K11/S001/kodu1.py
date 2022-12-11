def seosta_lapsed_ja_vanemad(koodid_f, nimed_f):
    koodid = open(koodid_f, "r", encoding="utf-8")
    nimed = open(nimed_f, "r", encoding="utf-8")
    
    nimed_sonastik = {}
    for rida in nimed:
        rida = rida.split(" ", 1)
        rida[1] = rida[1].replace("\n", "")
        nimed_sonastik[rida[0]] = rida[1]
    nimed.close()
    #print(nimed_sonastik)
    
    vanemad_sonastik = {}
    for rida in koodid:
        rida = rida.split()
        rida[1] = rida[1].replace("\n", "")
        if nimed_sonastik[rida[1]] in vanemad_sonastik.keys():
            vanemad_sonastik[nimed_sonastik[rida[1]]].add(nimed_sonastik[rida[0]])
        else:
            vanemad_sonastik[nimed_sonastik[rida[1]]] = {nimed_sonastik[rida[0]]}
    koodid.close()
    return vanemad_sonastik

seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")