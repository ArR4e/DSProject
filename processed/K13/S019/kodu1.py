def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    elif aastad == 1:
        return round(hind * (1 - (20/100)),2)
        
    else:
        return round(auto_hind(hind, aastad-1) *(1 - (20/100)),2)
    