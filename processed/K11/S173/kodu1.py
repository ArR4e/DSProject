def seosta_lapsed_ja_vanemad(a, b):
    koodid = open(a)
    nimed = open(b)
    lapsed = {}
    for i in koodid:
        laps = int(i.strip().split()[1])
        vanem = int(i.strip().split()[0])
        print(laps)
        print(vanem)
        if laps not in lapsed:
            lapsed[laps] = {vanem}
        else:
            lapsed[laps] = lapsed[laps].add(vanem)
    
    
    
    koodid.close()
    nimed.close()
    return(lapsed)
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))