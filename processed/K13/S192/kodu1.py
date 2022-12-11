def auto_hind(hind, aastad):
    if aastad == 0:
        uus_hind = hind
        return uus_hind
    else:
        uus_hind = round(hind - hind * 0.2, 2)
        return auto_hind(uus_hind, aastad-1)