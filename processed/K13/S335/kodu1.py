def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return auto_hind(round(hind-hind*0.20, 2), aastad-1)
