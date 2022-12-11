def seosta_lapsed_ja_vanemad(lapsed, nimed):
    nimikood = {}
    vanemlaps = {}
    f = open(lapsed,"r", encoding="UTF-8").readlines()
    tempkoodid = []
    for i in f:
        temp = None
        temp = i.replace("\n", "")
        temp2 = temp.split(" ")
        tempkoodid += temp2
    f = open(nimed,"r", encoding="UTF-8").readlines()
    tempkoodid2 = []
    for i in f:
        temp = None
        temp = i.replace("\n", "")
        temp2 = temp.split(" ",1)
        tempkoodid2 += temp2
    x = 0
    while x != len(tempkoodid2):
        nimikood[tempkoodid2[x]] = tempkoodid2[x+1]
        x += 2
    x = 1
    if len(tempkoodid) == 2: 
        vanemlaps[nimikood[tempkoodid[1]]] = set()
    elif len(tempkoodid) == 4: 
        vanemlaps[nimikood[tempkoodid[1]]] = set()
        vanemlaps[nimikood[tempkoodid[3]]] = set()
    elif len(tempkoodid) == 4: 
        vanemlaps[nimikood[tempkoodid[1]]] = set()
        vanemlaps[nimikood[tempkoodid[3]]] = set()
        vanemlaps[nimikood[tempkoodid[5]]] = set()
    else:
        while x != (len(tempkoodid)-1):
            vanemlaps[nimikood[tempkoodid[x]]] = set()
            x += 2
    x = 0
    for i in tempkoodid:
        if (x%2) != 0:
            vanemlaps[nimikood[i]].add(nimikood[tempkoodid[x-1]])
        else:
            pass
        x += 1
    #ärge küsige mis ma siin tegin ma tÕenäoliselt ei tea vastust
    #pärast 8t tundi und mis ma kohe saan.
    return vanemlaps