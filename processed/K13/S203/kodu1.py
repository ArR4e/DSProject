def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        hind = round(hind * 0.8, 2)
        return auto_hind(hind, aastad - 1)