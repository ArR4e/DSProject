def moos(suured_karbid, väikesed_karbid, kogus):
    karpide_arv = 0
    while True:
        if kogus - 5 > 0 and suured_karbid >= 1:
            kogus = kogus - 5
            suured_karbid = suured_karbid - 1
            karpide_arv = karpide_arv + 1
        elif suured_karbid == 1:
            break
        if väikesed_karbid >= kogus:
            kogus = kogus - 1
            väikesed_karbid = väikesed_karbid - 1
            karpide_arv = karpide_arv + 1
        elif väikesed_karbid == 1:
            break
        if kogus == 0:
            return karpide_arv
        else:
            print(-1)

suured = int(input("Sisestage suurte karpide kogus: "))
väikesed = int(input ("Sisestage väikeste karpide kogus: "))
moosi_kogus = int(input("Sisestage moosi kogus kilogrammides: "))
print(moos(1, 3, 7))

    