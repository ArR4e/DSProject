def moos(suurte_karpide_arv_on, väikeste_karpide_arv_on, moosi_kogus):
    if moosi_kogus % 5 > väikeste_karpide_arv_on:
        return -1
    elif suurte_karpide_arv_on < moosi_kogus // 5 and väikeste_karpide_arv_on < moosi_kogus - 5 * suurte_karpide_arv_on:
        return -1
    elif suurte_karpide_arv_on >= moosi_kogus // 5 and väikeste_karpide_arv_on >= moosi_kogus % 5:
        suurte_karpide_arv_onvaja = moosi_kogus // 5
        väikeste_karpide_arv_onvaja = moosi_kogus % 5
        return suurte_karpide_arv_onvaja + väikeste_karpide_arv_onvaja
    elif suurte_karpide_arv_on <= moosi_kogus // 5:
         suurte_karpide_arv_onvaja = suurte_karpide_arv_on
         väikeste_karpide_arv_onvaja = moosi_kogus - suurte_karpide_arv_onvaja * 5
         return suurte_karpide_arv_onvaja + väikeste_karpide_arv_onvaja
    
print(moos(0, 15, 20))
    
        
        


        
        
        
    
