def funktsioon(lastefail, nimedefail):
    lapsed_f = open(lastefail, "rt")
    nimed_f = open(nimedefail, "rt")
    v_ja_l_dict = {}
    nimed_dict = {}
    
    for rida in nimed_f:
        rida = rida.strip().split(" ", 1)
        nimed_dict[rida[0]] = rida[1]
    
    for rida in lapsed_f:
        rida = rida.strip().split(" ", 1)
        if nimed_dict[rida[1]] not in v_ja_l_dict:
            v_ja_l_dict[nimed_dict[rida[1]]] = {nimed_dict[rida[0]]}
        else:
            v_ja_l_dict[nimed_dict[rida[1]]].add(nimed_dict[rida[0]])
    lapsed_f.close()
    nimed_f.close()


    return v_ja_l_dict
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print(funktsioon("lapsed.txt","nimed.txt"))