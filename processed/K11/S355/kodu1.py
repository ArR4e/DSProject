def seosta_lapsed_ja_vanemad(lastefail, nimefail):
    avafail = open(lastefail)
    avafail2 = open(nimefail)
    isikulist2 = []
    nimelist2 = []
    lapsenimi = ""
    lapsenimed = []
    lapselist = set()
    vanemalist = set()
    lapsedic = {}
    vanemadic = {}
    lõppdic = {}
    
    for line in avafail:
        isikulist = line.split()
        isikulist2 += isikulist
    
    for line in avafail2:
        nimelist = line.split()
        nimelist2 += nimelist
        
    for el in isikulist2:
        if isikulist2.index(el) %2 == 1:
            lapselist.add(el)
        else:
            vanemalist.add(el)
    
    for el in nimelist2:
        if el in nimelist2 and el in lapselist and el in vanemalist:
           indeks = nimelist2.index(el)
           lapsedic[el] = nimelist2[indeks+1] + nimelist2[indeks+2]
           vanemadic[el] = nimelist2[indeks+1] + nimelist2[indeks+2]
        if el in nimelist2 and el in lapselist:
           indeks = nimelist2.index(el)
           lapsedic[el] = nimelist2[indeks+1] + nimelist2[indeks+2]
        elif el in nimelist2 and el in vanemalist:
            indeks = nimelist2.index(el)
            vanemadic[el] = nimelist2[indeks+1] + nimelist2[indeks+2]
           
    
    
    return isikulist2
        
    
lastefail = "lapsed.txt"
nimefail = "nimed.txt"

print(seosta_lapsed_ja_vanemad(lastefail, nimefail))