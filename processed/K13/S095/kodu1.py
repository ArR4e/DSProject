def auto_hind(hind,aastate_arv):
    if aastate_arv < 1:
        return hind
    else:
        return auto_hind(hind-(hind*0.2), aastate_arv-1)