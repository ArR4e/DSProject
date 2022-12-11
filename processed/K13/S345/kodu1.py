def auto_hind(alghind, aastate_arv):
    if aastate_arv == 0:
        return alghind
    else:
        return round(auto_hind(alghind*0.8, aastate_arv - 1), 2)