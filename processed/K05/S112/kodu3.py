
def moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus):
    suured_karbid = 0
    while moosi_kogus >= 5 and suurte_karpide_arv > 0:
        moosi_kogus -= 5
        suured_karbid += 1
        suurte_karpide_arv -= 1
        
    if moosi_kogus > väikeste_karpide_arv:
        return -1
    elif moosi_kogus < väikeste_karpide_arv:
        return suured_karbid + moosi_kogus
    elif moosi_kogus == väikeste_karpide_arv:
        return suured_karbid + väikeste_karpide_arv
    else:
        return suured_karbid
    

suurte_karpide_arv = int(input("Sisesta suurte karpide arv: "))
väikeste_karpide_arv = int(input("Sisesta väikeste karpide arv: "))
moosi_kogus = int(input("Sisesta moosi kogus kilogrammides: "))

print(moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus))