def auto_hind(hind, aastate_arv):
    if aastate_arv<=0:
        return hind
    else:
        uus_hind=auto_hind(round(hind*0.8, 2), aastate_arv-1)
        return uus_hind