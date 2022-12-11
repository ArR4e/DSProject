def auto_hind(hind,aastad):
    if aastad==0:
        hind=round(hind,2)
        return hind
    else:
        hind=round((hind-hind*0.2),2)
        return auto_hind(hind,aastad-1)