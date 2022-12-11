def moos(suured_karbid,vaiksed_karbid,moosi_kogus):
    moosi_kogus1 = moosi_kogus
    i = 1
    while i <= suured_karbid:
        print('a' + str(i))
        print('b' + str(moosi_kogus1))
        moosi_kogus1 -= 5
        if moosi_kogus1 == 0:
            vajalikud_suured_karbid = i
            break
        elif moosi_kogus1 < 0:
            vajalikud_suured_karbid = i - 1
            print(vajalikud_suured_karbid)
            break
        i += 1
    if suured_karbid * 5 + vaiksed_karbid < moosi_kogus:
        print(-1)
        return -1
    if moosi_kogus1 > 0:
        vajalikud_suured_karbid = suured_karbid
        vajalikud_vaiksed_karbid = moosi_kogus - vajalikud_suured_karbid * 5
        print(vajalikud_suured_karbid + vajalikud_vaiksed_karbid)
        return vajalikud_suured_karbid + vajalikud_vaiksed_karbid
    elif moosi_kogus1 == 0:
        print(vajalikud_suured_karbid)
        return vajalikud_suured_karbid
    elif moosi_kogus1 < 0:
        vahetehe = moosi_kogus - vajalikud_suured_karbid * 5
        print(vahetehe)
        if vaiksed_karbid >= vahetehe:
            vajalikud_vaiksed_karbid = vahetehe
            print(vajalikud_suured_karbid + vajalikud_vaiksed_karbid)
            return vajalikud_suured_karbid + vajalikud_vaiksed_karbid
        else:
            print(-1)
            return -1
    else:
        print(-1)
        return -1