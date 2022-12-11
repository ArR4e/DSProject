def seosta_lapsed_ja_vanemad(sõnastik1, sõnastik2):
    f1 = open(sõnastik1, encoding = "utf-8")
    f2 = open(sõnastik2, encoding = "utf-8")
    nimed = {}
    lapsed = {}
    
    for rida in f2:
        andmed = rida.strip().split(" ",1)
        nimed[andmed[0]] = [andmed[1]]

    for rida in f1:
        andmed = rida.strip().split()
        if nimed[andmed[1]][0] in lapsed:
            lapsed[nimed[andmed[1]][0]].add(nimed[andmed[0]][0])
        else:
            lapsed[nimed[andmed[1]][0]] = set(nimed[andmed[0]])
    
    f1.close()
    f2.close()
    return lapsed
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))