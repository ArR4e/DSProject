def auto_hind(hind,aastad):
    if aastad == 0:
        return round(hind,2)
    else:
        hind=round(hind*0.8,2)
        return auto_hind(hind,aastad-1)