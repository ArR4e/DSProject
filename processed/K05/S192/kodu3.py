def moos(suur_karp_arv, väike_karp_arv, moos_kg):
    karpide_arv = 0
    while True:
        while suur_karp_arv > 0 and moos_kg >= 5:
            moos_kg -= 5
            suur_karp_arv -= 1
            karpide_arv += 1
        while väike_karp_arv > 0 and moos_kg != 0:
            moos_kg -= 1
            väike_karp_arv -= 1
            karpide_arv += 1
        if moos_kg == 0:
            return karpide_arv
        else:
            return -1