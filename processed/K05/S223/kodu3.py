def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    karpide_kogus = 0
    if (suured_karbid*5 + väikesed_karbid) < moosi_kogus:
        return -1
    elif moosi_kogus == 0:
        return 0
    else:
        for x in range(suured_karbid):
            if moosi_kogus - 5 > 0:
                moosi_kogus = moosi_kogus - 5
                karpide_kogus += 1
            elif moosi_kogus - 5 == 0:
                return karpide_kogus + 1
        for x in range(väikesed_karbid):
            if moosi_kogus - 1 > 0:
                moosi_kogus = moosi_kogus - 1
                karpide_kogus += 1
            elif moosi_kogus - 1 == 0:
                return karpide_kogus + 1
        return -1