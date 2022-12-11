def moos(suurte_arv, väikeste_arv, kaal):
    karbid_kokku = 0
    while (kaal - 5) >= 0 and suurte_arv > 0:
        kaal -=  5
        suurte_arv -= 1
        karbid_kokku += 1
        if suurte_arv <= 0:
            break
    while (kaal - 1) >= 0:
        kaal -= 1
        väikeste_arv -= 1
        karbid_kokku += 1
        if väikeste_arv <= 0 and kaal > 0:
            karbid_kokku = -1
            break
    return(karbid_kokku)
suurte_arv =0
väikeste_arv =10
kaal = 7

moos(suurte_arv, väikeste_arv, kaal)
print(moos(suurte_arv, väikeste_arv, kaal))
            
    
    