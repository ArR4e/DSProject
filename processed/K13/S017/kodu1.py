def auto_hind(hind, aastad):
    if aastad == 0:
        return round(hind, 2)
    else:
        return round(auto_hind(hind, aastad - 1) * 0.8, 2)
