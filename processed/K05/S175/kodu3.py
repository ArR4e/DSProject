def moos(suuri_karpe, väikeseid_karpe, moosi_kogus):
    karpide_arv = 0
    while suuri_karpe > 0:
        moosi_kogus -= 5
        suuri_karpe -= 1
        karpide_arv += 1
        if moosi_kogus >= 0:
            moosi_kogus -= 1
            väikeseid_karpe -= 1
            karpide_arv += 1
        else:
            if moosi_kogus <= 0:
                moosi_kogus+=5
                karpide_arv-=1
                break
    if väikeseid_karpe >= moosi_kogus:
        karpide_arv += moosi_kogus
        return karpide_arv
    else:
        return -1