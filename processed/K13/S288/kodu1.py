def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        uus_hind = round(hind * 0.8, 2)
        return round(auto_hind(uus_hind, aastad - 1), 2)