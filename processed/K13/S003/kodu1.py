def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        return round(auto_hind(0.8 * hind , aastad -1), 2)