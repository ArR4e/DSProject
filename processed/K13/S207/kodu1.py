def auto_hind(hind, aastad):  
    if aastad > 0:
        return auto_hind(round(hind * 0.8, 2), aastad - 1)
    else:
        return round(hind, 2)