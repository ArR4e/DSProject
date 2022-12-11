def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        return auto_hind(round(hind-hind*0.2, 2), aastad-1)