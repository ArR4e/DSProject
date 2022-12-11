def seosta_lapsed_ja_vanemad(a,b):
    lapsed = open(a,"r")
    nimed = open(b,"r")
    t_lapsed = lapsed.readlines()
    t_nimed = nimed.readlines()
    lapsed.close()
    nimed.close()
    
    n = []
    d = {}
    
    for i in t_nimed:
        n += i.strip().split()
    
    for i in t_lapsed:
        l = i.strip().split()
        if (n[n.index(l[1])+1]+" "+n[n.index(l[1])+2]) in d:
            d[n[n.index(l[1])+1]+" "+n[n.index(l[1])+2]].add(n[n.index(l[0])+1]+" "+n[n.index(l[0])+2])
        else:
            d[n[n.index(l[1])+1]+" "+n[n.index(l[1])+2]] = {n[n.index(l[0])+1]+" "+n[n.index(l[0])+2]}
        
    return d