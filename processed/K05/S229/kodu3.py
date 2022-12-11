def moos(suured_karbid, väikesed_karbid, kogus):
    karpide_arv= 0
    while kogus >= 5:
        if suured_karbid >= 1:
            kogus = kogus - 5
            suured_karbid = suured_karbid - 1
            karpide_arv = karpide_arv + 1
        else:
            break
    while kogus >= 1:
        if kogus == väikesed_karbid:
            kogus = kogus - väikesed_karbid
            karpide_arv = karpide_arv + väikesed_karbid
        else:
            if väikesed_karbid > kogus:
                kogus = kogus - 1
                väikesed_karbid = väikesed_karbid - 1
                karpide_arv= karpide_arv + 1
            else:
                if kogus > väikesed_karbid:
                    karpide_arv = -1
                    break
    print(karpide_arv)
                
suured_karbid = int(input("Sisestage suurte karpide arv: "))
väikesed_karbid = int(input("Sisestage väikeste karpide arv: "))
kogus = int(input("Sisestage moosi kogus: "))
moos(suured_karbid, väikesed_karbid, kogus)