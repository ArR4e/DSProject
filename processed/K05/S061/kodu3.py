def moos(s_karpi_arv, v_karpi_arv, moosimass):
    if s_karpi_arv == 0 and v_karpi_arv >= moosimass:
        vaiksed_karbid = moosimass
        return vaiksed_karbid
    if s_karpi_arv < moosimass // 5 and v_karpi_arv < moosimass - 5 * s_karpi_arv:
        return -1
    elif moosimass % 5 > v_karpi_arv:
        return -1
    else:
        if s_karpi_arv > moosimass // 5:
            suuredkarbid = moosimass // 5
        elif s_karpi_arv <= moosimass // 5:
            suuredkarbid = s_karpi_arv
        vaiksedkarbid = moosimass - suuredkarbid * 5
        return suuredkarbid + vaiksedkarbid
    
print(moos(2, 6, 14))