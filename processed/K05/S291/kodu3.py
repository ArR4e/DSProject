def moos(suurte_karpide_arv, väikeste_karpide_arv, keedetava_moosi_kogus):
    suure_karbi_kaal = 5
    väikse_karbi_kaal = 1
    karpide_arv_kokku = 0
    
    while keedetava_moosi_kogus >= suure_karbi_kaal and suurte_karpide_arv != 0:
        keedetava_moosi_kogus -= suure_karbi_kaal
        karpide_arv_kokku += 1
        suurte_karpide_arv -= 1
    if suurte_karpide_arv == 0 and väikeste_karpide_arv == 0 and keedetava_moosi_kogus > 0:
        karpide_arv_kokku = -1
    
    while keedetava_moosi_kogus >= väikse_karbi_kaal and väikeste_karpide_arv != 0:
        keedetava_moosi_kogus -= väikse_karbi_kaal
        karpide_arv_kokku += 1
        väikeste_karpide_arv -= 1
    if väikeste_karpide_arv == 0 and keedetava_moosi_kogus > 0:
        karpide_arv_kokku = -1
        
    return karpide_arv_kokku

print(moos(1, 0, 5))
    