def auto_hind(autohind, aastad):
    autohind = float(autohind)
    autohind = round(autohind, 2)
    if aastad == 0:
        return autohind
    else:
        return auto_hind(autohind*80/100, aastad-1)