def auto_hind(hind,aastad):
    if aastad>=1:
        return hind-(hind-auto_hind(round(hind*0.8,2),aastad-1))
    else:
        return hind
