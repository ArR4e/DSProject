def moos(suur_karp, väike_karp, kogus):
    palju_kulub_suuri = suur_karp - (abs((kogus // 5) - suur_karp))
    if palju_kulub_suuri < 0:
        suurte_arv = abs(kogus // 5) - (abs((kogus // 5) - suur_karp))
    else:
        suurte_arv = suur_karp - (abs((kogus // 5) - suur_karp))
    palju_kuluks_väikseid = (kogus - (suurte_arv * 5)) // 1
    karpide_arv = suurte_arv + palju_kuluks_väikseid
    if palju_kuluks_väikseid > väike_karp:
        return -1
    else:
        return karpide_arv