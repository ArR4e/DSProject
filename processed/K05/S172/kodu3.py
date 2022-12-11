def moos(suurte_arv, vaikeste_arv, moosi_kogus):
    karbid_kokku = 0
    voimalik_moosi_kogus = 5*suurte_arv + vaikeste_arv
    
    if voimalik_moosi_kogus <= moosi_kogus:
        return -1
    
    vaja_suured = moosi_kogus // 5
    if vaja_suured <= suurte_arv:
        vaja_vaikesed = moosi_kogus % 5
        if vaja_vaikesed > vaikeste_arv:
            return -1
        karbid_kokku += vaja_suured + vaja_vaikesed
    else:
        moosi_kogus -= 5*suurte_arv
        vaja_vaikesed = moosi_kogus
        if vaja_vaikesed > vaikeste_arv:
            return -1
        karbid_kokku += suurte_arv + vaja_vaikesed
        
    return karbid_kokku

