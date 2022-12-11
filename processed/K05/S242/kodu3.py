import math

def moos(suuri_karpe, väikseid_karpe, moosi_kogus):
    suurte_karpide_arv = math.floor(moosi_kogus / 5)
    väikeste_karpide_arv = moosi_kogus - suurte_karpide_arv * 5
    if suurte_karpide_arv > suuri_karpe:
        väikeste_karpide_arv = (suurte_karpide_arv - suuri_karpe) * 5 + väikeste_karpide_arv
        if väikeste_karpide_arv > väikseid_karpe:
            return -1
        else:
            return väikeste_karpide_arv
    elif suuri_karpe * 5 + väikseid_karpe < moosi_kogus:
        return -1
    elif moosi_kogus / 5 < suuri_karpe:
        if moosi_kogus // 5 != 0:
            return -1
        else:
            return suurte_karpide_arv + väikeste_karpide_arv
    else:
        return suurte_karpide_arv + väikeste_karpide_arv
