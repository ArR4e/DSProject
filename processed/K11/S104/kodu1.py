def seosta_lapsed_ja_vanemad(iskukoodid, nimed):
    fail = open('isikukoodid.txt')
    koodid = fail.readlines()
    fail.close
    
    for i in range(len(koodid)):
        koodid[i] = koodid[i].strip('\n').split(' ')
    
    f = open('nimed.txt')
    seosed = f.readlines()
    f.close
    
    for i in range(len(seosed)):
        seosed[i] = seosed[i].strip('\n').split(' ')        