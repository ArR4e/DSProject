def auto_hind(hind, aastate_arv):
    if aastate_arv < 1:
        return hind
    else:
        h = 20
        uus = round(hind * (1-(h/100)),2)
        return auto_hind(uus, aastate_arv-1)