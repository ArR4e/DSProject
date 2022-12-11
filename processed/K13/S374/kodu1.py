def auto_hind(hind, aastad):
    protsent = 20
    
    if aastad == 0:
        return hind
    
    else:
        return auto_hind(round(hind*(1-(protsent/100)),2), aastad-1)
    
