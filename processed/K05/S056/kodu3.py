def moos(suur_karp,väike_karp,moosi_kogus):
    kogus = (suur_karp * 5) + väike_karp
    if kogus < moosi_kogus:
        return -1
    else:
        if suur_karp == 0 and väike_karp == 0 and moosi_kogus == 0:
            return -1
        else:
            suurivaja = moosi_kogus // 5
            suuri_kasutada = min(suurivaja,suur_karp)
            väikseidvaja = moosi_kogus - (suuri_kasutada * 5)
            karpe_vaja = suuri_kasutada + väikseidvaja
            if väikseidvaja > väike_karp:
                return -1
            else:
                return karpe_vaja