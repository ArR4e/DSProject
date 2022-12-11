def auto_hind(hind, aastad):
    if aastad > 0:
        return auto_hind(hind*0.8, aastad-1)
    else:
        return round(hind, 2)
