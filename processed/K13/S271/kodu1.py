def auto_hind(hind, aastad):
    if aastad > 0:
        hind = round(hind*0.8, 2)
        aastad -= 1
        return round(auto_hind(hind, aastad), 2)
    else:
        return hind