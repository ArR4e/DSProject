def auto_hind(hind,aastad):
    if aastad==0:
        return hind
    else:
        return round(0.8*auto_hind(hind,aastad-1),2)