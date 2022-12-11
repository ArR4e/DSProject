def auto_hind(hind, aastad):
    uus_hind = round((hind * (1 - (20/100))), 2)
    if aastad == 0:
        return hind
    else:
        return auto_hind(uus_hind, aastad-1)
    