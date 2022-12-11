def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return auto_hind(0.8*hind, aastad - 1)