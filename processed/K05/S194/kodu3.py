def moos(s_arv, v_arv , m):
    kasutatud_karpide_kogus = 0
    kasutatud_v = 0
    kasutatud_s = 0
    algne_m = m
    while m >= 5:
        m -= 5
        s_arv -= 1
        kasutatud_s += 1
        kasutatud_karpide_kogus += 1
        if s_arv == 0:
            break
    while m  >= 1:
        m -= 1
        kasutatud_v += 1
        v_arv -= 1
        kasutatud_karpide_kogus += 1
        if v_arv == 0:
            break

    if algne_m/(kasutatud_s*5 + kasutatud_v) != 1:
        kasutatud_karpide_kogus = -1
    
    return kasutatud_karpide_kogus