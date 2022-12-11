def auto_hind(a_hind, aastad):
    if aastad != 0:
        a_hind = round((a_hind*0.8),2)
        aastad -= 1
        return auto_hind(a_hind, aastad)
    else:
        return a_hind