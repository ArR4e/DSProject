def moos(suur_karp,väike_karp,moosi_kogus):
    karpide_arv = 0
    while moosi_kogus > 0:
        if moosi_kogus >= 5 and suur_karp > 0:
            moosi_kogus -= 5
            suur_karp -= 1
            karpide_arv += 1
        elif moosi_kogus >= 5 and väike_karp > 0:
            moosi_kogus -= 1
            väike_karp -= 1
            karpide_arv += 1
        elif moosi_kogus < 5 and väike_karp > 0:
            moosi_kogus -= 1
            väike_karp -= 1
            karpide_arv += 1
        else:
            return -1
    return karpide_arv