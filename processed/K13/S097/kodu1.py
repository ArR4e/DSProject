def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        uus_hind = auto_hind(hind * 0.8, aastad - 1)
        return round(uus_hind, 2)