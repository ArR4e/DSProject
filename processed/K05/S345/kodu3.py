def moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus):
    if suurte_karpide_arv < int(moosi_kogus/5):
        kasutatavad_suured = suurte_karpide_arv
    else:
        kasutatavad_suured = int(moosi_kogus/5)

    suurte_maht = 5*kasutatavad_suured
    
    if väikeste_karpide_arv < moosi_kogus - suurte_maht:
        kasutatavad_väiksed = väikeste_karpide_arv
    else:
        kasutatavad_väiksed = moosi_kogus - suurte_maht
        
    if suurte_maht + kasutatavad_väiksed == moosi_kogus:
        karpide_arv = kasutatavad_suured + kasutatavad_väiksed
        return karpide_arv
    else:
        return -1