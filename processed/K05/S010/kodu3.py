def moos(suuredkarbid, väiksedkarbid, moosikogus):
    karpide_kogus=0
    if moosikogus>=5:
        suurte_jääk=moosikogus%5
    else:
        suurte_jääk=0
    suuri_karpe=(moosikogus-suurte_jääk)//5 # Potentsiaalselt vajalike suurte karpide arv
    if suuredkarbid<suuri_karpe:
        suuri_karpe=suuredkarbid
    väikeste_arv=moosikogus-suuri_karpe*5 # Potentsiaalselt vajalike väikeste karpide arv
    if suuredkarbid*5 + väiksedkarbid<moosikogus:
        return int(-1)
    if suuri_karpe==0:
        if väiksedkarbid>=moosikogus:
            return moosikogus
        else:
            return int(-1)
    elif suuredkarbid<suuri_karpe and väiksedkarbid>=väikeste_arv:
        karpide_kogus+=suuri_karpe + väikeste_arv
        return int(karpide_kogus)
    elif suuredkarbid>=suuri_karpe and väiksedkarbid<väikeste_arv:
        if suuri_karpe*5+väiksedkarbid>=moosikogus:
            karpide_kogus+=suuri_karpe+väikeste_arv
            return int(karpide_kogus)
        else:
            return int(-1)
    elif suuredkarbid>=suuri_karpe and väiksedkarbid>=väikeste_arv:
        karpide_kogus+= suuri_karpe + väikeste_arv
        return int(karpide_kogus)
    else:
        return int(-1)