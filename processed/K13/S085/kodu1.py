def auto_hind(hind, aastad):
    uus_hind = hind * (1 - 0.2)
    if aastad == 1:
        return round(uus_hind, 2)
    elif aastad == 0:
        return hind
    else:
        return auto_hind(uus_hind, aastad-1)
