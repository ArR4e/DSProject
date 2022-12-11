def auto_hind(autohind, aastad):
    if aastad == 0:
        return autohind
    else:
        return round((auto_hind(autohind, aastad - 1) * 0.80), 2)