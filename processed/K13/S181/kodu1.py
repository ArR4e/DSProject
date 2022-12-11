def auto_hind(hind,aastad):
    if aastad == 0:
        return hind
    else:
        aastad -= 1
        hind = round(hind * 0.8,2)
        return auto_hind(hind, aastad)