def auto_hind(hind, aastad):
    if aastad == 0:
        return(round(hind, 2))
    else:
        return(auto_hind(0.8 * hind, aastad-1))
    
