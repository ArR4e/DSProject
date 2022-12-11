def seosta_lapsed_ja_vanemad(laste_fail,nimede_fail): 
    d = open(laste_fail)
    id_number,nimed,koos = [],{},{} 
    for rida in d:
        id_number += [rida.split()]
    d.close()
    f = open(nimede_fail)
    for rida in f:
        nimi = rida.split()
        nimed[nimi[0]]=nimi[1]+" "+nimi[2]
    f.close()
    a=0
    sonastik = {}
    for el in id_number:
        if nimed[el[1]] in sonastik:
            sonastik[nimed[el[1]]].add(nimed[el[0]])
        else:
            sonastik[nimed[el[1]]]={nimed[el[0]]}  
    return(sonastik)
seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")