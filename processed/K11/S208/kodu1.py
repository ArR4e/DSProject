def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f1 = open(lapsed)
    f2 = open(nimed)
    sõnastik = {}
    nimed = {}
    lapsed = {}
    for rida in f1:
        jrj = rida.strip().split()
        if (jrj[1] in lapsed) == False:
            lapsed[jrj[1]] = set()
        lapsed[jrj[1]].add(jrj[0])
    for rida in f2:
        jrj = rida.strip().split(" ", 1)
        nimed[jrj[0]] = jrj[1]
    for el in lapsed:
        sõnastik[nimed[el]] = set()
    for el in lapsed:
        vanemad = lapsed[el]
        for vanem in vanemad:
            sõnastik[nimed[el]].add(nimed[vanem])      
    f1.close()
    f2.close()
    return sõnastik
vastus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for el in vastus:
    vanemad = ""
    for v in vastus[el]:
        if vanemad != "":
            vanemad += ", "
        vanemad += v
    print(el +":",vanemad)