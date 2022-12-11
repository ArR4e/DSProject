def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        return auto_hind(hind/5*4, aastad-1)