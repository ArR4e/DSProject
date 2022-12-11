def moos(suurte_karpide_arv, vaikeste_karpide_arv, moosi_kogus):
    moosi_suurtes_karpides=suurte_karpide_arv*5
    vaikeseid_karpe_vaja=moosi_kogus-(suurte_karpide_arv*5)
    kokku_karpe=0
    if vaikeseid_karpe_vaja<=0:
        suuri_karpe_vaja=moosi_kogus//5
        vaikeseid_karpe_vaja=moosi_kogus-(suuri_karpe_vaja*5)
        if vaikeseid_karpe_vaja<=vaikeste_karpide_arv:
            return (suuri_karpe_vaja + vaikeseid_karpe_vaja)
        else:
            return (-1)
    elif moosi_suurtes_karpides<=moosi_kogus and type(moosi_suurtes_karpides)==int and vaikeseid_karpe_vaja<=vaikeste_karpide_arv and type(vaikeseid_karpe_vaja)==int:
        kokku_karpe+=suurte_karpide_arv
        kokku_karpe+=vaikeseid_karpe_vaja
        return (kokku_karpe)
    else:
        return (-1)

    

